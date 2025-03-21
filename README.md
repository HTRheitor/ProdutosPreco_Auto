# Product Price Update Automation

## Important Notice
**WARNING:** All system URLs, credentials, and file paths included in this repository are **FICTIONAL** and created for demonstration purposes only. The sample HTML page is a mock-up of the actual admin panel. All real client data, website details, and authentication information have been removed to preserve privacy and security.

## About the Project
This project automates the daily process of updating product prices in an admin panel. The automation script navigates to the admin panel, scrolls through to load all products, and uploads an Excel spreadsheet containing the updated prices.

![Captura de tela 2025-03-21 123450](https://github.com/user-attachments/assets/5d4c9d50-fe69-4801-9eb1-1a9c80bcbbac)

### Features
- Automated login to admin panel
- Automatic scrolling to load all products (including "load more" functionality)
- File upload automation using Selenium and PyAutoGUI
- Simple, reliable process that saves time on daily price updates

## Requirements
- Python 3.6 or higher
- Libraries:
  - selenium
  - pyautogui
  - webdriver-manager (recommended)
- Chrome browser and compatible ChromeDriver

## File Structure
- `app.py` - Main automation script
- `sample_page.html` - Fictional representation of the admin panel (for demonstration)
- `precos-produtos-atualizados.xlsx` - Example of price data file (not included - use your own file)

## How to Use
1. Update the file path in the script to point to your Excel file with product prices
2. Run the script:
```bash
python app.py
```
3. The script will automatically:
   - Open the admin panel
   - Scroll to load all products
   - Click the "Carregar mais" button to display additional products
   - Click the "Subir Planilha de Preços" button
   - Enter the file path to your Excel sheet
   - Wait for your confirmation to close

## Important Notes
- The script includes a deliberate pause at the end requiring manual intervention (pressing Enter) to allow verification of successful upload
- This ensures that the process completes successfully before closing


## Troubleshooting
If you encounter issues:
1. Ensure ChromeDriver is compatible with your Chrome version
2. Check that the XPath selectors still match the website elements
3. Adjust sleep times if the website is responding slowly
