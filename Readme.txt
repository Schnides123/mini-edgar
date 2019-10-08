Hi, thanks for taking the time to check out my edgar crawler!

I threw it together using Scrapy and BeautifulSoup, so there shouldn't be too many dependencies with running everything. 

If there are any problems with installation or your computer catches on fire while running the program, 
feel free to reach out to me any time at aas339@cornell.edu.

=================

Steps to install:

1.      Use pip to install the following dependencies:
            -Scrapy
            -BeautifulSoup

1.5.    Make sure your paths are set up to be able to run scrapy from the command line. To check whether or not this is the case,
            just type "scrapy" into the command line and see if anything comes up. (I tried doing a test install on a friend's computer,
            and this was a pain to deal with. That said, I'd imagine an office machine would be already configured and that
            this will probably be a non-issue for you.)

2.      Navigate to src/edgar-crawler

3.      Use the following command to run the crawler:

            scrapy crawl crawler [-a cik_ticker=""] [-a output_path=""] [-a output_name=""]

            *using -a cik_ticker=#### isn't required, but it'll prompt you to enter one in later if you don't
            **By default, the output path is set to the data folder in src/edgar-crawler
            ***If you don't include a name for the output file, it'll be named after the CIK or Ticker