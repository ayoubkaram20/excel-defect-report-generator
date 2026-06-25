import pandas as pd
import glob

try:
    # Search for any Excel file (.xlsx) in the current folder
    excel_files = glob.glob("*.xlsx")

    # Exclude the generated report if it already exists
    excel_files = [file for file in excel_files if "rapport_defauts" not in file]

    if not excel_files:
        print("❌ Error: No Excel file found in this folder!")
    else:
        # Take the first Excel file found
        input_file = excel_files[0]
        print(f"🔄 Processing file: {input_file}")

        # Read the Excel file
        df = pd.read_excel(input_file)

        # Filter defective items and calculate total quantity
        defective_items = df[df['Statut'] == 'Défectueux']
        total_defective_quantity = defective_items['Quantité'].sum()

        # Save defective items to a new report
        output_file = "rapport_defauts.xlsx"
        defective_items.to_excel(output_file, index=False)

        print("--- Bright Sud Automation: Success ---")
        print(f"✔ Total defective parts: {total_defective_quantity}")
        print(f"✔ File '{output_file}' created successfully!")

except Exception as error:
    print(f"❌ An error occurred during processing: {error}")