---
layout: post
permalink: /api/create
---

<h1>FE POST new user</h1>

<form id="addUserForm">
  <label for="firstName">First Name:</label>
  <input type="text" id="firstName" name="firstName" required><br>
  <label for="lastName">Last Name:</label>
  <input type="text" id="lastName" name="lastName" required><br>
  <label for="residence">Residence:</label>
  <input type="text" id="residence" name="residence" required><br>
  <button type="submit">Add User</button>
</form>
<div id="addUserResult"></div>

<script>
  // Handle form submission action
  document.getElementById('addUserForm').addEventListener('submit', function (event) {
    event.preventDefault();
    // gather form data
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const residence = document.getElementById('residence').value;
    // prepare data object in JSON format
    const data = {
      FirstName: firstName,
      LastName: lastName,
      Residence: residence
    };

    // prepare fetch payload
    const url = 'http://localhost:5001/api/data';
    const options = {
      method: 'POST',
      mode: 'cors',
      cache: 'default',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data) 
    };

    // perform fetch to add user
    fetch(url, options)
      // Always extract JSON, then handle error or success
      .then(response => response.json()
        .then(json => {
          if (!response.ok) {
            throw new Error(json.message || json.error || `Fetch error: status ${response.status}`);
          }
          return json.body; // User details are wrpped in body
        })
        // on success, show user added through fetch
        .then(user => {
          const message = `Added ID ${user.id}: ${user.FirstName} ${user.LastName} from ${user.Residence}`;
          document.getElementById('addUserResult').innerHTML = `<span style="color:green">${message}</span>`;
        }))
      // on failure, catch the fetch error and display message
      .catch(error => {
        document.getElementById('addUserResult').innerHTML = `<span style='color:red'>${error}</span>`;
        console.error(error);
      });
  });
</script>

