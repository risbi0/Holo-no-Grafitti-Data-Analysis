## Holo no Grafitti Data Analysis

* `main.ipynb` - analyzes the dataset made by `extract_comments.py` by generating a word cloud and other visualizations. `jp.ipynb` for JP comments
* `scripts/extract_comments.py` - extracts comments from all the comment sections of HoloGra episodes from the Hololive official Youtube channel using the Youtube Data API. It saves every comment in a single file in `datasets/hologra_comments.csv`.
* `scripts/hologra_mem_analysis.py` - makes two csv files from a manually-defined set of arrays listing the episode numbers of each Holomem that had an appearance on HoloGra. One basically transformed to a csv file saved in `datasets/appearance_record.csv`, and one transformed as incremental data saved as `datasets/appearance_timeline.csv`. Both files are used for visualizations in an MS Excel file.
* `scripts/misc.js` - collection of Javascript codes used in extracting data from a web browser.