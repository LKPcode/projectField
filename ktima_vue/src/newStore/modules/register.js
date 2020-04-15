import axios from 'axios'

const register = {
    state: {
        isLoggedin: false,
        token: ""
    },

    async sign_in(username, password) {
        try {
            const response = await axios
                .post("http://localhost:9000/api/user/login/", {
                    username: username,
                    password: password
                })
            console.log(response)
            this.state.token = response.data.token;
            this.state.isLoggedin = true;
            return response.status;

        } catch (error) {
            console.log("Error: " + error.request.status + "   " + this.getCookie("token"))
            return error.request.status;
        }


    },
    async sign_up(register) {
        try {
            const response = await axios
                .post("http://localhost:9000/api/user/", {
                    email: register.email,
                    username: register.username,
                    password: register.password_1
                })
            console.log(response)
            this.state.token = response.data.token;
            this.state.isLoggedin = true;
            return response.status;

        } catch (error) {
            console.log("Error: " + error.request.status + "   " + this.getCookie("token"))
            return error.request.status;
        }


    },
    getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length == 2)
          return parts
            .pop()
            .split(";")
            .shift();
      },


};

export default register