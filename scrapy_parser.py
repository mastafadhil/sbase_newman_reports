import scrapy

class SeleniumBaseTestReportSpider(scrapy.Spider):
    name = 'seleniumbase_test_report'
    start_urls = ['C://Users//fadhil.HALOCHECK//OneDrive - Halocheck Sdn Bhd//Documents//sbase_newman_report//sbase_report.html']  # Replace with the path to your SeleniumBase report file

    def parse(self, response):
        # Extract information from test results
        test_results = response.css('col-name')

        for test_result in test_results:
            test_name = test_result.css('.test-name::text').get()
            test_status = test_result.css('.test-status::text').get()

            # Process the extracted data (store in a data structure, print, etc.)
            yield {
                'Test': test_name,
                'Status': test_status
            }