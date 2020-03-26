# Matplotlib implementations

This repository contains examples of many types of charts using [Matplotlib](https://matplotlib.org/) library.
These files were created following some Youtube Channels:
- [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)
- [sentdex](https://www.youtube.com/user/sentdex/featured)


## Using the correct chart

This guide reference is a copy and paste [EasyBi Blog's post](https://eazybi.com/blog/data_visualization_and_chart_types/).

### Tables

Tables are essentially the source for all the charts. They are best used for comparison, composition, or relationship analysis when there are only few variables and data points. It would not make much sense to create a chart if the data can be easily interpreted from the table.

> **Use tables** when:
- You need to compare or look up individual values.
- You require precise values.
- Values involve multiple units of measure.
- The data has to communicate quantitative information, but not trends.

> **Use charts** when the data presentation:
- Is used to convey a message that is contained in the shape of the data.
- Is used to show a relationship between many values.

### Column Charts

The column chart is probably the most used chart type. This chart is best used to compare different values when specific values are important, and it is expected that users will look up and compare individual values between each column. With column charts you could compare values for different categories or compare value changes over a period of time for a single category.

> **Best practices for column charts**
- Use column charts for comparison if the number of categories is quite small — up to five, but not more than seven categories.
- If one of your data dimensions is time — including years, quarters, months, weeks, days, or hours — you should always set time dimension on the horizontal axis.
- If one of your data dimensions is time — including years, quarters, months, weeks, days, or hours — you should always set time dimension on the horizontal axis.
- For column charts, the numerical axis must start at zero. Our eyes are very sensitive to the height of columns, and we can draw inaccurate conclusions when those bars are truncated.
- Avoid using pattern lines or fills. Use border only for highlights.
- Only use column charts to show trends if there are a reasonably-low number of data points (less than 20) and if every data point has a clearly-visible value.

#### Column Histograms

Histogram is a common variation of column charts used to present distribution and relationships of a single variable over a set of categories. A good example of a histogram would be a distribution of grades on a school exam or the sizes of pumpkins, divided by size group, in a pumpkin festival.

#### Stacked Column Charts

Use stacked column charts to show a composition. Do not use too many composition items (not more than three or four) and make sure the composing parts are relatively similar in size. It can get messy very quickly. Before moving to the next chart type, I wanted to show you a good example of how to improve the effectiveness of your column chart by simplifying it. Credit: [Joey Cherdarchuk](https://speakerdeck.com/player/87bb9f00ec1e01308020727faa1f9e72)

### Bar Charts

Bar charts are essentially horizontal column charts. If you have long category names, it is best to use bar charts because they give more space for long text. You should also use bar charts, instead of column charts, when the number of categories is greater than seven (but not more than fifteen) or for displaying a set with negative numbers.

- A typical use of bar charts would be visitor traffic from top referral websites. Referring sites are usually more than five to seven sites and website names are quite long, so those should be better horizontally graphed.
- Another example could be sales performance by sales representatives. Again, names can be quite long, and there might be more than seven sales reps.

#### Bar Histogram Charts

Just like column charts, bar charts can be used to present histograms.

- A good histogram example is a population distribution by the age (and sex). Remember those Christmas-tree graphs?

#### Stacked Bar Charts

I’m not quite sure about a good application of stacked bar charts — except when there are only a few variables, composition parts, and the emphasis is on composition, not comparison. Stacked bars are not good for comparison or relationship analysis. The only common baseline is along the left axis of the chart, so you can only reliably compare values in the first series and for the sum of all series.

### Line Charts

Who doesn’t know line charts? We used to draw those on blackboards in school. Line charts are among the most frequently used chart types. Use lines when you have a continuous data set. These are best suited for trend-based visualizations of data over a period of time, when the number of data points is very high (more than 20).
With line charts, the emphasis is on the continuation or the flow of the values (a trend), but there is still some support for single value comparisons, using data markers (only with less than 20 data points.) A line chart is also a good alternative to column charts when the chart is small.

#### Timeline Charts

The timeline chart is a variation of line charts. Obviously, any line chart that shows values over a period of time is a timeline chart. The only difference is in functionality — most timeline charts will let you zoom in and out and compress or stretch the time axis to see more details or overall trends.
The most common examples of a time-line chart might be:
- stock market price changes over time,
- website visitors per day for the past 30 days,
- sales numbers by day for the previous quarter.

#### The Dos and Don’ts for Line Charts

- Use lines to present continuous data in an interval scale, where intervals are equal in size.
- For line charts, the axis may not start from zero if the intended message of the chart is the rate of change or overall trend, not exact values or comparison. It’s best to start the axis with zero for wide audiences because some people may otherwise interpret the chart incorrectly.
- In line charts, time should always run from left to right.
- Do not skip values for consistent data intervals presenting trend information, for example, certain days with zero values.
- Remove guidelines to emphasize the trend, rate of change, and to reduce distraction.
- Use a proper aspect ratio to show important information and avoid dramatic slope effects. For the best perception, aim for a 45-degree slope. (https://eagereyes.org/basics/banking-45-degrees )

### Area Charts

An area chart is essentially a line chart — good for trends and some comparisons. Area charts will fill up the area below the line, so the best use for this type of chart is for presenting accumulative value changes over time, like item stock, number of employees, or a savings account. Do not use area charts to present fluctuating values, like the stock market or prices changes.

#### Stacked Area

Stacked area charts are best used to show changes in composition over time. A good example would be the changes of market share among top players or revenue shares by product line over a period of time. Stacked area charts might be colorful and fun, but you should use them with caution, because they can quickly become a mess. Don’t use them if you need an exact comparison and don’t stack together more than three to five categories.

### Pie Charts and Donut Charts

Who doesn’t love pies or donuts, right? Not in data visualization, though. These charts are among the most frequently used and also misused charts. The one on the right is a good example of a terrible, useless pie chart - too many components, very similar values. A pie chart typically represents numbers in percentages, used to visualize a part to whole relationship or a composition. Pie charts are not meant to compare individual sections to each other or to represent exact values (you should use a bar chart for that).

#### Stacked Donut Charts

I would not recommend using stacked donut charts at all! I mean, like, never! You might think that you could use a stacked donut to present composition, while allowing some comparison (with an emphasis on composition), but it would perform badly for both. Use stacked column charts instead.

#### The Dos and Don’ts for Pie charts

- Make sure that the total sum of all segments equals 100 percent.
- Use pie charts only if you have less than six categories, unless there’s a clear winner you want to focus on.
- Ideally, there should be only two categories, like men and women visiting your website, or only one category, like a market share of your company, compared to the whole market.
- Don’t use a pie chart if the category values are almost identical or completely different. You could add labels, but that’s a patch, not an improvement.
- Don’t use 3D or blow apart effects — they reduce comprehension and show incorrect proportions.

### Scatter Charts 

Scatter charts are primarily used for correlation and distribution analysis. Good for showing the relationship between two different variables where one correlates to another (or doesn’t). Scatter charts can also show the data distribution or clustering trends and help you spot anomalies or outliers. A good example of scatter charts would be a chart showing marketing spending vs. revenue.

#### Bubble Charts

A bubble chart is a great option if you need to add another dimension to a scatter plot chart. Scatter plots compare two values, but you can add bubble size as the third variable and thus enable comparison. If the bubbles are very similar in size, use labels. We could in fact add the fourth variable by color-grading those bubbles or displaying them as pie charts, but that’s probably too much. A good example of a bubble chart would be a graph showing marketing expenditures vs. revenue vs. profit. A standard scatter plot might show a positive correlation for marketing costs and revenue (obviously), when a bubble chart could reveal that an increase in marketing costs is chewing on profits.

> Use Scatter and Bubble charts to:

- Present relationships between two (scatter) or three (bubble) numerical variables,
- Plot two or three sets of variables on one x-y coordinate plane,
- Turn the horizontal axis into a logarithmic scale, thus showing the relationships between more widely distributed elements.
- Present patterns in large sets of data, linear or non-linear trends, correlations, clusters, or outliers.
- Compare large number of data points without regard to time. The more data you include in a scatter chart, the better comparisons you can make.
- Present relationships, but not exact values for comparisons.

### Data Visualization Do’s and Don’ts – A General Conclusion

- Time axis. When using time in charts, set it on the horizontal axis. Time should run from left to right. Do not skip values (time periods), even if there are no values.
- Proportional values. The numbers in a chart (displayed as bar, area, bubble, or other physically measured element in the chart) should be directly proportional to the numerical quantities presented.
- Data-Ink Ratio. Remove any excess information, lines, colors, and text from a chart that does not add value. More about data-Ink ratio
- Sorting. For column and bar charts, to enable easier comparison, sort your data in ascending or descending order by the value, not alphabetically. This applies also to pie charts.
- Legend. You don’t need a legend if you have only one data category.
- Labels. Use labels directly on the line, column, bar, pie, etc., whenever possible, to avoid indirect look-up.
- Inflation adjustment. When using monetary values in a long-term series, make sure to adjust for inflation. (EU Inflation rates, US InflationM rates)
- Colors. In any chart, don’t use more than six colors.
- Colors. For comparing the same value at different time periods, use the same color in a different intensity (from light to dark).
- Colors. For different categories, use different colors. The most widely used colors are black, white, red, green, blue, and yellow.
- Colors. Keep the same color palette or style for all charts in the series, and same axes and labels for similar charts to make your charts consistent and easy to compare.
- Colors. Check how your charts would look when printed out in grayscale. If you cannot distinguish color differences, you should change hue and saturation of colors.
- Colors. Seven to 10 percent of men have color deficiency. Keep that in mind when creating charts, ensuring they are readable for color-blind people. Use Vischeck to test your images. Or, try to use color palettes that are friendly to color-blind people.
- Data Complexity. Don’t add too much information to a single chart. If necessary, split data in two charts, use highlighting, simplify colors, or change chart type. Credit: Junkcharts