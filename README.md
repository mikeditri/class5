# class5
OPEN ME WITH TEXT EDITOR

00. Basic: Write Psuedocode for how to A) load, B) "organize", C) compute summary statistics (all A-C were done in class today), D) Visualize the data, 1-feature (column) at a time, i.e. histogram, and save the figures to files E) Visualize the data, 2-features (columns) at a time, i.e. scatter plot, and save the figures to files,
000. (intermediate) F) Pseudocode for adding header data to your table, for an arbitrary one of these datasets,
0000. (reach) G) Pseudocode for an additional type of plot (Google to find plot types of interest) for visualizing 2 or more of the features at a time.
Recommendation: plan to use `matplotlib` for plotting

0. Load data
0.1   Import data file

1. Format & Organize
1.1   Import numpy
1.2   Import pandas
1.3   Read data file using pandas library and deternmine if there is a header row or not
1.3.1      pandas.read_csv(my_csv_file, Header=None)
1.4   View the shape of the data

2. Summary Statistics
2.1   Use Numpy to calculate summary statistics like mean, standard deviation etc
2.1.1      numpy.mean(data)
2.1.2      numpy.std(data)

3. Add Headers
3.1   test if csv has a header
3.1.1 Import csv library
3.1.2 run csv sniffer
3.2   if csv does not have header:
			Create a header.csv file in the same shape as the data
     		Import the header.csv
            for each column:
                append data to header
      else move to next step

4. Look at it
4.1 Plot values on histograms
    import matplotlib
4.1.1  for each column:
           get values
           plot histogram
           save to file as column_name.png

4.2 Plot pairs
4.2.1  for each pair of columns:
           plot scatter
           save to file as column_name1_vs_column_name2_scatter.png

4.3 Plot pair-wise correlation matrix as a heatmap


