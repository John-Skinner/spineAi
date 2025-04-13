# spineAi
on linux, may need to install a package
```
sudo apt install python3-venv
```
Then follow the following steps to start the server
```
cd src
./pipInstalls.sh
python3 -m venv myenv
source myenv/bin/active
python3 app.py

```
After the server is running, open another terminal and cd to the 
src directory.
```
./runcurl.sh
```
This will send the spine request down to the server.
The server's (app.py) autospinelabel function will fill a numpy array, shorts with the image.
The function currently has dummy code to send back 3 points.  These
are in image coordinates.
