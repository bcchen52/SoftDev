DISCO:

Multiple methods to generate secret key 

```
import secrets

app.secret_key = secret.token.hex()

```

or 

```
import os

app.secret_key = os.urandom(12)

```

ALSO redirecting to a function

```
import redirect, url_for 

@app.route("/1")
def index():
    pass


@app.route("/2")
def function():
    return redirect(url_for('index'))
...