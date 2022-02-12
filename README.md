<h4> Store sales prediction </h4>
<p>This is a web application to predict the sales of an Item at store,
where user have to provide some information about item and can get prediction. <br>
Running at: <a href="https://sales-prediction123.herokuapp.com/">https://sales-prediction123.herokuapp.com/</a></p>
<h4>Dataset</h4>
<p>Dataset is taken from kaggle, <a href="https://www.kaggle.com/brijbhushannanda1979/bigmart-sales-data">dataset_link</a></p>
<h4>Data description</h4>
<p>We have total 8523 data points and 12 columns in train.csv file </p>

|                  Variable	             |      Description                                                                             |
|---|--- |
|Item_Identifier	                       |  Unique product ID                                                                           |                                      
|Item_Weight	                           |  Weight of product                                                                           |
|Item_Fat_Content	                       |   Whether the product is low fat or not                                                      |
|Item_Visibility	                       |   The % of total display area of all products in a store allocated to the particular product |
|Item_Type	                             |   The category to which the product belongs                                                  |
|Item_MRP	                               |   Maximum Retail Price (list price) of the product                                           |
|Outlet_Identifier	                     |   Unique store ID                                                                            |
|Outlet_Establishment_Year	             |   The year in which store was established                                                    |
|Outlet_Size	                           |  The size of the store in terms of ground area covered                                       |
|Outlet_Location_Type	                   |  The type of city in which the store is located                                              |
|Outlet_Type	                           |  Whether the outlet is just a grocery store or some sort of supermarket                      |
|Item_Outlet_Sales	                     |Sales of the product in the particular store. This is the outcome variable to be predicted.   |
 
<h4>Model</h4>
<p>After cleaning and preprocessing we have trained a machine learning model
with RMSE of 1091.96</p>

<h4> Flask</h4>
<p>we used flask for building API</p>

<h4>Deployment</h4>
<p>we have deployed this application on <strong>Heroku</strong></p>