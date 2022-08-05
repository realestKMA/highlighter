/* eslint-disable */
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from "axios";
import FlagIcon from "vue-flag-icon";

import './assets/index.css'

// axios settings
axios.defaults.baseURL = "http://localhost:8000/api/";
// axios.defaults.baseURL = "http://192.168.1.102:8000/api/";
axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.withCredentials = true;
axios.defaults.timeout = 9000;

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(FlagIcon);

app.mount('#app')
