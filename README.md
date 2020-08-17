---


---

<h1 id="project-data-warehouse">Project: Data Warehouse</h1>
<h2 id="bintroductionb"><b>Introduction</b></h2>
<p>A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.</p>
<p>Task is to build an ETL Pipeline that extracts their data from S3, staging it in Redshift and then transforming data into a set of Dimensional and Fact Tables for their Analytics Team to continue finding Insights to what songs their users are listening to.</p>
<h2 id="bproject-descriptionb"><b>Project Description</b></h2>
<p>Application of Data warehouse and AWS to build an ETL Pipeline for a database hosted on Redshift Will need to load data from S3 to staging tables on Redshift and execute SQL Statements that create fact and dimension tables from these staging tables to create analytics</p>
<h2 id="bproject-datasetsb"><b>Project Datasets</b></h2>
<p>Here are the S3 links for each:</p>
<ul>
<li>Song data:  <code>s3://udacity-dend/song_data</code></li>
<li>Log data:  <code>s3://udacity-dend/log_data</code></li>
</ul>
<p>Log data json path:  <code>s3://udacity-dend/log_json_path.json</code></p>
<h2 id="bsong-datasetb"><b>Song Dataset</b></h2>
<p>The first dataset is a subset of real data from the <a href="https://labrosa.ee.columbia.edu/millionsong/">Million Song Dataset</a>. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song’s track ID.<br>
For example, here are filepaths to two files in this dataset.</p>
<pre><code>song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
</code></pre>
<p>And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.</p>
<pre><code>{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
</code></pre>
<h2 id="blog-datasetb"><b>Log Dataset</b></h2>
<p>The second dataset consists of log files in JSON format generated by this  <a href="https://github.com/Interana/eventsim">event simulator</a>  based on the songs in the dataset above. These simulate app activity logs from an imaginary music streaming app based on configuration settings.</p>
<p>The log files in the dataset you’ll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.</p>
<pre><code>log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
</code></pre>
<p>And below is an example of what a single log file, 2018-11-13-events.json, looks like.</p>
<pre><code>{"artist":"Pavement", 
"auth":"Logged In", 
"firstName":"Sylvie", 
"gender", "F", 
"itemInSession":0, 
"lastName":"Cruz", 
"length":99.16036, 
"level":"free", 
"location":"Klamath Falls, OR", 
"method":"PUT", 
"page":"NextSong", 
"registration":"1.541078e+12", 
"sessionId":345, 
"song":"Mercy:The Laundromat", 
"status":200, 
"ts":1541990258796, 
"userAgent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_9_4...)", 
"userId":10}
</code></pre>
<h2 id="bschema-for-song-play-analysisb"><b>Schema for Song Play Analysis</b></h2>
<p>A Star Schema would be required for optimized queries on song play queries</p>
<h4 id="fact-table">Fact Table</h4>
<ol>
<li><strong>songplays</strong>  - records in event data associated with song plays i.e. records with page  <code>NextSong</code>
<ul>
<li><em>songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent</em></li>
</ul>
</li>
</ol>
<h4 id="dimension-tables">Dimension Tables</h4>
<ol start="2">
<li><strong>users</strong>  - users in the app
<ul>
<li><em>user_id, first_name, last_name, gender, level</em></li>
</ul>
</li>
<li><strong>songs</strong>  - songs in music database
<ul>
<li><em>song_id, title, artist_id, year, duration</em></li>
</ul>
</li>
<li><strong>artists</strong>  - artists in music database
<ul>
<li><em>artist_id, name, location, lattitude, longitude</em></li>
</ul>
</li>
<li><strong>time</strong>  - timestamps of records in  <strong>songplays</strong>  broken down into specific units
<ul>
<li><em>start_time, hour, day, week, month, year, weekday</em></li>
</ul>
</li>
</ol>
<h2 id="project-template">Project Template</h2>
<p>To get started with the project, go to the workspace on the next page, where you’ll find the project template. You can work on your project and submit your work through this workspace.</p>
<p>Alternatively, you can download the template files in the Resources tab in the classroom and work on this project on your local computer.</p>
<p>The project template includes four files:</p>
<ul>
<li><code>create_table.py</code>  is where you’ll create your fact and dimension tables for the star schema in Redshift.</li>
<li><code>etl.py</code>  is where you’ll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.</li>
<li><code>sql_queries.py</code>  is where you’ll define you SQL statements, which will be imported into the two other files above.</li>
<li><code>README.md</code>  is where you’ll provide discussion on your process and decisions for this ETL pipeline.</li>
</ul>
<h2 id="project-steps">Project Steps</h2>
<p>Below are steps you can follow to complete each component of this project.</p>
<h3 id="create-table-schemas">Create Table Schemas</h3>
<ol>
<li>Design schemas for your fact and dimension tables</li>
<li>Write a SQL  <code>CREATE</code>  statement for each of these tables in  <code>sql_queries.py</code></li>
<li>Complete the logic in  <code>create_tables.py</code>  to connect to the database and create these tables</li>
<li>Write SQL  <code>DROP</code>  statements to drop tables in the beginning of  <code>create_tables.py</code>  if the tables already exist. This way, you can run  <code>create_tables.py</code>  whenever you want to reset your database and test your ETL pipeline.</li>
<li>Launch a redshift cluster and create an IAM role that has read access to S3.</li>
<li>Add redshift database and IAM role info to  <code>dwh.cfg</code>.</li>
<li>Test by running  <code>create_tables.py</code>  and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.</li>
</ol>
<h3 id="build-etl-pipeline">Build ETL Pipeline</h3>
<ol>
<li>Implement the logic in  <code>etl.py</code>  to load data from S3 to staging tables on Redshift.</li>
<li>Implement the logic in  <code>etl.py</code>  to load data from staging tables to analytics tables on Redshift.</li>
<li>Test by running  <code>etl.py</code>  after running  <code>create_tables.py</code>  and running the analytic queries on your Redshift database to compare your results with the expected results.</li>
<li>Delete your redshift cluster when finished.</li>
</ol>
<h2 id="bfinal-instructionsb"><b>Final Instructions</b></h2>
<ol>
<li>Import all the necessary libraries.</li>
<li>Write the configuration of AWS Cluster, store the important parameter in some other file.</li>
<li>Configuration of boto3 which is an AWS SDK for Python.</li>
<li>Using the bucket, can check whether files log files and song data files are present.</li>
<li>Create an IAM User Role, Assign appropriate permissions and create the Redshift Cluster.</li>
<li>Get the Value of Endpoint and Role for put into main configuration file.</li>
<li>Authorize Security Access Group to Default TCP/IP Address.</li>
<li>Launch database connectivity configuration.</li>
<li>Go to Terminal write the command <code>python create_tables.py</code> and then <code>python etl.py</code>.</li>
<li>Should take around 4-10 minutes in total.</li>
<li>Then you go back to jupyter notebook to test everything is working fine.</li>
<li>I counted all the records in my tables.</li>
<li>Now can delete the cluster, roles and assigned permission.</li>
</ol>
<blockquote>
<p>Written with <a href="https://stackedit.io/">StackEdit</a>.</p>
</blockquote>

