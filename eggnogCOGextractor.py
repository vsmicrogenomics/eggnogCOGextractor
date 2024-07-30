import os
import pandas as pd

# Function to extract COG information and generate the output
def process_emapper_annotations(input_file_path, output_folder):
    # Read the data with the specified column names
    columns = [
        "#query",
        "seed_ortholog",
        "evalue",
        "score",
        "eggNOG_OGs",
        "max_annot_lvl",
        "COG_category",
        "Description",
        "Preferred_name",
        "GOs",
        "EC",
        "KEGG_ko",
        "KEGG_Pathway",
        "KEGG_Module",
        "KEGG_Reaction",
        "KEGG_rclass",
        "BRITE",
        "KEGG_TC",
        "CAZy",
        "BiGG_Reaction",
        "PFAMs"
    ]

    # Read the data skipping the unnecessary rows
    data = pd.read_csv(input_file_path, sep='\t', names=columns, skiprows=4, skipfooter=3, engine='python')

    # Initialize dictionaries to store COG counts and descriptions
    cog_counts = {}
    cog_descriptions = {}

    # COG ID to Description mapping
    cog_id_to_description = {
        'A': 'RNA processing and modification',
        'B': 'Chromatin structure and dynamics',
        'C': 'Energy production and conversion',
        'D': 'Cell cycle control, cell division, and chromosome partitioning',
        'E': 'Amino acid transport and metabolism',
        'F': 'Nucleotide transport and metabolism',
        'G': 'Carbohydrate transport and metabolism',
        'H': 'Coenzyme transport and metabolism',
        'I': 'Lipid transport and metabolism',
        'J': 'Translation, ribosomal structure, and biogenesis',
        'K': 'Transcription',
        'L': 'Replication, recombination, and repair',
        'M': 'Cell wall/membrane/envelope biogenesis',
        'N': 'Cell motility',
        'O': 'Post-translational modification, protein turnover, and chaperones',
        'P': 'Inorganic ion transport and metabolism',
        'Q': 'Secondary metabolites biosynthesis, transport, and catabolism',
        'R': 'General function prediction only',
        'S': 'Function unknown',
        'T': 'Signal transduction mechanisms',
        'U': 'Intracellular trafficking, secretion, and vesicular transport',
        'V': 'Defense mechanisms',
        'W': 'Extracellular structures',
        'Y': 'Nuclear structure',
        'Z': 'Cytoskeleton'
    }

    # Iterate through each row of the DataFrame
    for _, row in data.iterrows():
        cog_categories = row['COG_category'].split(',')  # Split multiple COG categories
        descriptions = row['Description'].split(',')  # Split multiple descriptions

        for i, cog_category in enumerate(cog_categories):
            cog_category = cog_category.strip()  # Remove leading/trailing spaces

            # Split multiple COG letters
            cog_letters = cog_category.split('|')

            for cog_letter in cog_letters:
                cog_letter = cog_letter.strip()  # Remove leading/trailing spaces

                cog_ids = cog_letter.split()  # Split multiple COG IDs

                for cog_id in cog_ids:
                    cog_id = cog_id.strip()  # Remove leading/trailing spaces

                    # Skip the 'COG_category' label and '-'
                    if cog_id != 'COG_category' and cog_id != '-':
                        if len(cog_id) > 1:
                            # If the COG ID has more than one character, split it
                            for letter in cog_id:
                                cog_counts[letter] = cog_counts.get(letter, 0) + 1  # Increment count
                                cog_descriptions[letter] = f"[{letter}] {cog_id_to_description.get(letter, 'Unknown')}"  # Assign description
                        else:
                            cog_counts[cog_id] = cog_counts.get(cog_id, 0) + 1  # Increment count
                            cog_descriptions[cog_id] = f"[{cog_id}] {cog_id_to_description.get(cog_id, 'Unknown')}"  # Assign description

    # Calculate the total number of COG categories
    total_cog_categories = sum(cog_counts.values())

    # Calculate the total count
    total_count = sum(cog_counts.values())

    # Extract the input file name without extension
    input_file_name = os.path.basename(input_file_path)
    file_name_without_extension = os.path.splitext(input_file_name)[0]

    # Generate the output file name with the '.cog.tsv' extension
    output_file_name = f"{file_name_without_extension}.cog.tsv"

    # Create the full path for the output file in the output folder
    output_file_path = os.path.join(output_folder, output_file_name)

    # Sort COG IDs alphabetically
    sorted_cog_ids = sorted(cog_counts.keys())

    # Write the results to the output file
    with open(output_file_path, 'w') as output_file:
        # Write the header
        output_file.write("COGID\tCOGDescription\tCOGCount\tCOGPercentage\n")

        # Write COG ID, COG Description, COG Count, and COG Percentage
        for cog_id in sorted_cog_ids:
            description = cog_descriptions[cog_id]
            count = cog_counts[cog_id]
            percentage = (count / total_count) * 100
            output_file.write(f"{cog_id}\t{description}\t{count}\t{percentage:.2f}\n")

# Input folder containing .emapper.annotations files
input_folder = 'input'

# Output folder to save .cog.tsv files
output_folder = 'output'

# Process all .emapper.annotations files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".emapper.annotations"):
        input_file_path = os.path.join(input_folder, filename)
        process_emapper_annotations(input_file_path, output_folder)
