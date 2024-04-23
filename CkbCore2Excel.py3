import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        gene_links = soup.select('a.btn.btn-block.btn-gene, a.btn.btn-block.btn-custom-default')
        data_entries = []
        for link in gene_links:
            gene_name = link.get_text(strip=True)
            full_url = "https://ckb.jax.org" + link['href']
            gene_id = link['href'].split('=')[1]
            record_type = 'CKB BOOST' if 'btn-custom-default' in link['class'] else 'CKB CORE'
            if record_type == 'CKB CORE':
                data_entries.append([gene_name, full_url, gene_id, record_type])
        return pd.DataFrame(data_entries, columns=['Gene Name', 'URL', 'Gene ID', 'Type'])
    else:
        print(f"Failed to retrieve the webpage: HTTP {response.status_code}")
        return pd.DataFrame()

def fetch_data(url, table_class):
    response = requests.get(url)
    data, headers = [], []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_=table_class)
        if table:
            headers = [th.get_text(strip=True) for th in table.find_all('th')]
            rows = table.find_all('tr')[1:]  # Skip header row
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    row_data = [col.text.strip() for col in cols]
                    data.append(row_data)
        else:
            print(f"No table found with class '{table_class}' at {url}")
    else:
        print(f"Failed to retrieve data from {url}: HTTP {response.status_code}")
    return data, headers

def main():
    url = "https://ckb.jax.org/gene/grid"
    df = fetch_and_parse(url)

    table_classes = {
        'GeneVariants': 'gene_variant_tab_table',
        'CategoryVariants': 'category_variants_tab_table',
        'MolecularProfiles': 'molecular-profile-tab-table',
        'Evidence': 'profile-response-table-without-treatment-approach',
        'ClinicalTrials': 'clinical-trial-standard-layout'
    }

    tab_types = {
        'GeneVariants': 'GENE_VARIANTS',
        'CategoryVariants': 'CATEGORY_VARIANTS',
        'MolecularProfiles': 'MOLECULAR_PROFILES',
        'Evidence': 'GENE_LEVEL_EVIDENCE',
        'ClinicalTrials': 'CLINICAL_TRIALS'
    }

    # Prepare empty DataFrames with appropriate column names
    tabs_df = {name: pd.DataFrame() for name in table_classes.keys()}

    for _, row in df.iterrows():
        for name, table_class in table_classes.items():
            tab_url = f"{row['URL']}&tabType={tab_types[name]}"
            fetched_data, headers = fetch_data(tab_url, table_class)
            if fetched_data and headers:
                temp_df = pd.DataFrame(fetched_data, columns=headers)
                tabs_df[name] = pd.concat([tabs_df[name], temp_df], ignore_index=True)

    # Writing to Excel without index
    excel_path = '../Data/CKB_Gene_Data.xlsx'
    with pd.ExcelWriter(excel_path) as writer:
        df.to_excel(writer, sheet_name='GeneSummary', index=False)
        for name, data in tabs_df.items():
            data.to_excel(writer, sheet_name=name, index=False)

    print(f"Data written to {excel_path}")
    return df, tabs_df

# Run main function and get DataFrames
df_extended, tabs_data = main()
print(df_extended)  # Example to print one DataFrame
