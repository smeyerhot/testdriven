import React from 'react';

const Chat = (props) => {
  return (
    <div>
      <center><h1>Contact List</h1></center>
      {props.movies.map((movie) => (
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{props.movie.name}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{props.contact.email}</h6>
            <p class="card-text">{props.contact.company.catchPhrase}</p>
          </div>
        </div>
      ))}
    </div>
  )

}

export default Chat;
