def generate_overall_report(selenium_data, newman_data):
    # Read the overall QA report template
    with open('overall_template.html', 'r') as file:
        template = file.read()

    # Insert Selenium data into the template
    selenium_report_section = '\n'.join([f'<li>{test}</li>' for test in selenium_data])
    template = template.replace('{{selenium_report}}', selenium_report_section)

    # Insert Newman data into the template
    newman_report_section = '\n'.join([f'<li>{test}</li>' for test in newman_data])
    template = template.replace('{{newman_report}}', newman_report_section)

    # Write the final report to a new HTML file
    with open('overall_report.html', 'w') as file:
        file.write(template)

# Example data (replace with actual parsed data)
selenium_data = ['Test 1: Passed', 'Test 2: Failed']
newman_data = ['API Test 1: Passed', 'API Test 2: Passed']

# Generate the overall QA report
generate_overall_report(selenium_data, newman_data)