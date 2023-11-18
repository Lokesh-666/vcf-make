import pandas as pd

def csv_to_vcf(csv_file, vcf_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Check if required columns exist in the DataFrame
    required_columns = ['Name', 'Phone']
    if not all(column in df.columns for column in required_columns):
        missing_columns = [column for column in required_columns if column not in df.columns]
        print(f"Error: Missing required columns: {missing_columns}")
        return

    # Create a function to format each row as a vCard string
    def format_as_vcard(row):
        return f"BEGIN:VCARD\nVERSION:3.0\nFN:{row['Name']}\nTEL:{row['Phone']}\nEND:VCARD"

    # Apply the formatting function to each row and join the results
    vcard_strings = df.apply(format_as_vcard, axis=1)

    # Write the vCard strings to a VCF file
    with open(vcf_file, 'w') as vcf:
        for vcard_string in vcard_strings:
            vcf.write(vcard_string + '\n\n')

    print(f"Conversion successful. VCF file '{vcf_file}' created.")

# Replace 'input.csv' with your CSV file name and 'output.vcf' with the desired VCF file name
csv_to_vcf('input.csv', 'output.vcf')
