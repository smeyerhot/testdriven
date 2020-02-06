import React, { Component } from 'react';
import Chat from './Chat';
import axios from 'axios';

class Chatroom extends Component {
    constructor (props) {
        super(props);
        this.state = { 
            contacts: []
        };

    };
    //route /queue/tasks
    componentDidMount() {
      fetch(`${process.env.REACT_APP_USERS_SERVICE_URL}/chat`)
      .then(res => res.json())
      .then((data) => {
        this.setState({ contacts: data })
      })
      .catch(console.log)
      }
      
    
    // makeid(length) {
    //     var result           = '';
    //     var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    //     var charactersLength = characters.length;
    //     for ( var i = 0; i < length; i++ ) {
    //        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    //     }
    //     return result;
    //  }

    // postTasks(event) {
    //     const options = {
    //         url: `${process.env.REACT_APP_CHAT_SERVICE_URL}/people `,
    //         method: 'get',
    //         headers: {
    //           'Content-Type': 'application/json',
    //           Authorization: `Bearer ${window.localStorage.authToken}`
    //         }
    //       };
    //     return axios(options)
          
    //       .then((res) => {
    //         const contacts = res.data.data.children.map(obj => obj.data);
    //         this.setState({ contacts })
    //       })
    //       .catch(console.log)
    //       // .then((res) => {
    //       //   this.setState({
    //       //     task: res.data.data.task,
              
          
    //       };
    //     //   .done((res) => {
    //     //     getStatus(res.data.task_id)
    //     //   })
    //       .catch((error) => { console.log(error); });
    //     };

    render() {
        return (

          <Chat contacts={this.state.contacts} />
        // getApiInfo() {
        );
    }
}

export default Chatroom;