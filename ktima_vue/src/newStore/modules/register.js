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
            return true;

        } catch (error) {
            console.log("Error: " + error.request.status + this.getCookie("token"))
            return false;
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