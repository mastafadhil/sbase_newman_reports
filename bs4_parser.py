from bs4 import BeautifulSoup

def parse_pytest_html_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Find all table rows containing test results
        test_results = soup.find_all('tr', class_='col-name')

        # Extract information from each test result
        """for test_result in test_results:
            # Test name is usually contained within the first <a> tag inside the <td> with class 'col-name'
            test_name = test_result.find('td', class_='col-name').a.text

            # Test status is usually contained within the <span> tag with class 'col-result'
            test_status = test_result.find('td', class_='empty log').span.text

            # Extract more information as needed...
            
            # Process the extracted data (store in a data structure, print, etc.)
            print(f'Test: {test_name}, Status: {test_status}')"""
        print (test_results)

# Usage
parse_pytest_html_report('C://Users//fadhil.HALOCHECK//OneDrive - Halocheck Sdn Bhd//Documents//sbase_newman_report//sbase_report.html')
