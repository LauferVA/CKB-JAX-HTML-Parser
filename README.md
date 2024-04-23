# CKB-JAX-HTML-Parser
This repository contains a very short workflow that parses the CKB CORE data housed at https://ckb.jax.org/

**Notes**:

These data were pulled using the attached parse script, which was run in Python 3.11. An env file is provided and can install necessary modules provided that pip3 is present and the user has appropriate permissions.
Briefly, the source HTML in the main gene page is used to build the first table (housed in the CKB_CORE tab). The links in this page are used to identify the individual gene pages. The remaining tabs are populated by parsing each single-gene page.
Each single gene page has multiple tabs. In this spreadsheet, all 49 CKB CORE genes are put together. However, each tab in the single gene pages corresponds to a single tab in this spreadsheet.
No representation is made that the data provided are exhaustive, complete, etc. Code is provided for transparency - further validation is solely the responsibility of the user. Notably, CKB-JAX itself is not and cannot be complete as data are curated manually and by request. Caveat Emptor.
As the original data are licensed according to CC 4.0 (see below), so the data redacted here and the code used to compile this spreadsheet is as well.
For this spreadsheet: Date of Access 4-22-2024; 18:30. The database pull and curation operations are subject to the curation procedures of CKB-JAX itself at this time point, as laid forth on the site and as limited by https://ckb.jax.org/about/disclaimer.
For terms, glossary, curation information, etc. please see: https://ckb.jax.org/about/curationMethodology 
Contact: For comments, questions, etc., please use either vlaufer@med.umich.edu or laufer@openchromatin.com

**Known_Issues**:

The data provided differ somewhat from the raw output of the python functions provided. Specifically, 5 or so regular expressions were used to clean raw output (e.g., multi-line fields). Changes to content are not made.
Manual inspection indicate that some of the data itself could be regarded as suspect or definitions used as somewhat arbitrary. As an example, consider the information contained in the EfficacyEvidence tab related to the N549K variant in FGFR2.
Several tabs Refer to Variants on a certain genetic background (e.g., KRAS G12D TP53 WT). These entries are not always parsed exhaustively.
Several tabs contain multiple entries per row; e.g. EML4-ALK;ALK then in the adjacent column Var1;Var2. These entries are not always parsed exhaustively.
In a small number of cases, variant nomenclature other than that correspondent to the appropriate transcript isoform are provided. These are rare and are usually noted as such only within the description or evidence column - not in the main variant column.
These data are for the 50 CKB CORE Entries, as listed here: https://ckb.jax.org/gene/grid as the data are publically available and licensed according to CC BY-NC-SA 4.0 DEED (see https://creativecommons.org/licenses/by-nc-sa/4.0/).
There are an additional ~2000 CKB BOOST Entries not included in this HTML scrape. These could, presumably, be obtained similarly. However, if this is desired, please verify with CKB-JAX those data are also licensed as in the field above prior to contacting at above email.
