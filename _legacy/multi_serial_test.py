from pathos.multiprocessing import ProcessingPool as Pool #pip install pathos


class Parser(Subject):
    def __init__(self):
        self.pool = Pool(processes=3)
        
    def open_browser(self, site):
        driver = webdriver.Chrome('./chromedriver.exe')
        driver.get(site)
        
    def multi_processing(self):
    	sites = ['https://www.naver.com', 'https://www.daum.net', 'https://www.tistory.com']
    	pool.map(open_browser, browsers)
        
        
        
parser = Parser()
parser.multi_processing()