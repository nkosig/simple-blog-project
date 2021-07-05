// import Cookies from 'js-cookie';
import axios from 'axios';

// const token = Cookies.get('id_token');
const baseDomain = 'http://127.0.0.1:8084';
// const authorization_prefix = 'Beaer ';

export const customHeaders = {
    'Content-Type': 'application/json',
    Accept: 'application/json'
    //Authorization: authorization_prefix + token || undefined
};

export const baseUrl = `${baseDomain}`;

export const httpClient = axios.create({
    baseUrl,
    headers: customHeaders
});

export const serializeQuery = query => {
    return Object.keys(query)
        .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(query[key])}`)
        .join('&');
};
