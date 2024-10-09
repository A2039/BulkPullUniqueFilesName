import os
import pandas as pd
from tqdm import tqdm

# Function to validate folder path input
def validate_input_path(prompt):
    while True:
        folder_path = input(f"Enter the path for {prompt}: ")
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            return folder_path
        print(f"❌ Invalid folder path: {folder_path}. Please enter a valid path.")

# Function to validate Excel filename input
def validate_excel_name():
    while True:
        excel_name = input("Enter the Excel filename (without extension): ")
        if excel_name.strip():
            return f"{excel_name.strip()}.xlsx"
        print("❌ Excel file name cannot be empty.")

def get_files(folder_path):
    files_set = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            files_set.add(file)
    return files_set

def create_excel(data, excel_path):
    df = pd.DataFrame(list(data), columns=['unique_script_from_both_folder'])
    df.to_excel(excel_path, index=False, engine='openpyxl')

# Main function to execute the script
def main():
    try:
        # Validating folder inputs and Excel filename
        folder1 = validate_input_path("Folder 1")
        folder2 = validate_input_path("Folder 2")
        output_folder = validate_input_path("Folder to save Excel file")
        excel_name = validate_excel_name()

        excel_path = os.path.join(output_folder, excel_name)

        print("🚀 Processing file comparison...")

        files_folder1 = get_files(folder1)
        files_folder2 = get_files(folder2)

        unique_files = files_folder1.union(files_folder2)

        # Progress bar for the number of unique files processed
        with tqdm(total=len(unique_files), desc="Comparing files", ncols=100, colour="green") as progress_bar:
            for _ in unique_files:
                progress_bar.update(1)

        # Creating the Excel file from the unique SQL files
        create_excel(unique_files, excel_path)
        print(f"✅ Process complete. 🐍 Results saved at: {excel_path}")

    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

# Running the main function when the script is executed
if __name__ == '__main__':
    main()
