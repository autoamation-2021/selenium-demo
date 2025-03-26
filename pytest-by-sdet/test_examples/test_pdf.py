# import asyncio
# from pyppeteer import launch

# async def generate_pdf():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://meylah.com/')  # Load your webpage
#     await page.pdf({'path': 'output.pdf', 'format': 'A4'})
#     await browser.close()

# asyncio.run(generate_pdf())
# print("PDF generated successfully!")

#==================================================================================

# from playwright.sync_api import sync_playwright

# def generate_pdf():
#     with sync_playwright() as p:
#         # Launch a headless browser (supports Chromium, Firefox, WebKit)
#         browser = p.chromium.launch()
#         page = browser.new_page()
        
#         # Load local HTML file
#         with open("template.html", "r", encoding="utf-8") as file:
#             html_content = file.read()
        
#         # Set HTML content and wait for JavaScript execution
#         page.set_content(html_content)
#         page.wait_for_timeout(2000)  # Wait 2 seconds for JavaScript to execute
        
#         # Generate PDF
#         page.pdf(path="output.pdf", format="A4", print_background=True)
        
#         browser.close()

# # Run PDF generation
# generate_pdf()
# print("PDF generated successfully!")

#=====================================================================================

# from weasyprint import HTML
# import matplotlib.pyplot as plt
# import os

# # Generate a Chart Image using Matplotlib
# def generate_chart():
#     plt.figure(figsize=(5, 3))  # Set figure size
#     data = [10, 20, 15, 30, 25]
#     labels = ['A', 'B', 'C', 'D', 'E']
    
#     plt.bar(labels, data, color='skyblue')
#     plt.xlabel("Categories")
#     plt.ylabel("Values")
#     plt.title("Sample Chart")
    
#     chart_path = "chart.png"
#     plt.savefig(chart_path, bbox_inches='tight')  # Save chart as an image
#     plt.close()
#     return chart_path

# # Generate Chart and Embed in HTML
# chart_path = generate_chart()

# # HTML Content
# html_content = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>PDF Report</title>
#     <style>
#         body {{
#             font-family: Arial, sans-serif;
#             padding: 20px;
#         }}
#         h1 {{
#             text-align: center;
#         }}
#         .chart-container {{
#             text-align: center;
#             margin-top: 20px;
#         }}
#         .data-table {{
#             width: 100%;
#             border-collapse: collapse;
#             margin-top: 20px;
#         }}
#         .data-table th, .data-table td {{
#             border: 1px solid #ddd;
#             padding: 8px;
#             text-align: center;
#         }}
#         .data-table th {{
#             background-color: #f4f4f4;
#         }}
#     </style>
# </head>
# <body>
#     <h1>PDF Report with Charts</h1>

#     <div class="chart-container">
#         <img src="{chart_path}" width="500" />
#     </div>

#     <table class="data-table">
#         <tr>
#             <th>Category</th>
#             <th>Value</th>
#         </tr>
#         <tr><td>A</td><td>10</td></tr>
#         <tr><td>B</td><td>20</td></tr>
#         <tr><td>C</td><td>15</td></tr>
#         <tr><td>D</td><td>30</td></tr>
#         <tr><td>E</td><td>25</td></tr>
#     </table>
# </body>
# </html>
# """

# # Convert HTML to PDF
# pdf_path = "output.pdf"
# HTML(string=html_content).write_pdf(pdf_path)

# # Cleanup chart image after PDF generation
# os.remove(chart_path)

# print(f"PDF generated successfully: {pdf_path}")

# import weasyprint

# # HTML content as a string
# html_content = """
# <html>
#     <head>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#             }
#             h1 {
#                 color: #2C3E50;
#             }
#             p {
#                 font-size: 14px;
#                 color: #34495E;
#             }
#             .highlight {
#                 color: red;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>Sample PDF Report</h1>
#         <p>This is a <span class="highlight">sample</span> paragraph with HTML content.</p>
#         <ul>
#             <li>Item 1</li>
#             <li>Item 2</li>
#             <li>Item 3</li>
#         </ul>
#     </body>
# </html>
# """

# # Convert HTML to PDF
# pdf_file = "sample_report.pdf"
# weasyprint.HTML(string=html_content).write_pdf(pdf_file)

# print(f"PDF saved as {pdf_file}")


# import locale

# # Set to the user's default locale
# locale.setlocale(locale.LC_ALL, '')

# number = 1234567890
# formatted_number = locale.format_string("%d", number, grouping=True)
# print(formatted_number)  # Output varies based on locale, e.g., '1,234,567,890' in the US

# pip install Babel
from babel.numbers import format_decimal

# Example number
number = 12345678911011.2222344

# Format number for U.S. locale
formatted_number = format_decimal(number,format='#,##0.00', locale='en_US')
print(formatted_number)  # Output: 123,456,789.222
