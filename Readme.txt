Hi, thanks for taking the time to check out my edgar crawler!

I threw it together using Scrapy and BeautifulSoup, so there shouldn't be too many dependencies with running everything. 

Additionally, I've got ahead and included my venv config. It might be convenient to use them for setup, but you mileage may vary. The installation instructions below will assume that you aren't using them.

If there are any problems with installation or your computer catches on fire while running the program, feel free to reach out to me any time at aas339@cornell.edu.

=================

Steps to install:

1.      Use pip to install the following dependencies:
            -Scrapy
            -BeautifulSoup

1.5.    Make sure your paths are set up to be able to run scrapy from the command line. To check whether or not this is the case, just type "scrapy" into the command line and see if anything comes up. 

        (I tried doing a test install on a friend's computer and this was a bit of a pain to deal with. That said, I'd imagine an office machine would be already configured so this will probably be a non-issue for you.)

2.      Navigate to src/edgar-crawler

3.      Use the following command to run the crawler:

            scrapy crawl crawler [-a cik_ticker=""] [-a output_path=""] [-a output_name=""]

            *using -a cik_ticker=#### isn't required, but it'll prompt you to enter one in later if you don't
            **By default, the output path is set to the data folder in src/edgar-crawler
            ***If you don't include a name for the output file, it'll be named after the CIK or Ticker

        For reference, here are the example values from the prompt:

        Gates Foundation | 0001166559 
        CALEDONIA FUND LTD. | 0001037766
        Peak6 Investments LLC | 0001756111 
        Kemnay Advisory Services Inc. | 0001555283 
        HHR Asset Management, LLC | 0001397545 
        Benefit Street Partners LLC | 0001543160 
        Okumus Fund Management Ltd. | 0001496147 
        PROSHARE ADVISORS LLC | 0001357955 
        TOSCAFUND ASSET MANAGEMENT LLP | 0001439289 
        Black Rock | 0001086364