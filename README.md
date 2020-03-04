# Delivery-assignment

 ## Installation

###Below step is for ubuntu <br/>
   Before doing anything you have to clone or download(and unzip) the project folder, open terminal and navigate to the project folder and run:

   ```
   virtualenv -p python3 venv
   source venv/bin/activate
   pip install -r requirements.txt
  
   ```

   This will install all the dependencies required by the project.


### Running the server

```
python manage.py runserver

```


### Api endpoints

   <table>
   	<tr>
   		<th>S.No.</th>
   		<th>Route</th>
   		<th>Method</th>
   		<th>Access</th>
   		<th>Description</th>
   	</tr>	
	<tr>
   	   <td>1</td>
           <td>localhost:8000/get-cost/</td>
           <td>POST</td>
           <td>Public</td>
           <td>return minimum cost</td>
   	</tr>
   </table>



### Input


```
Add raw data as an input :
{
	"A":"1",
	"B":"1",
	"C":"1",
	"D":"1"

}
```
```
output : 
{
    "cost": 168.0
}
```

### Demo
   ![img1](./demo/demo.png) <br>
