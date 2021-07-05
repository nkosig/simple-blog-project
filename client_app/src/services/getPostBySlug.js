import { httpClient, baseUrl } from '../utils/httpClient';

export async function getPostBySlug() {
    // const endPoint = `${serializeQuery(payload)}`;
    const reponse = await httpClient.get(`${baseUrl}/posts`)
        .then(response => {
            console.log(response);
            if (response.data && response.data.posts.length > 0) {
                return response.data.posts;
            } else {
                return null;
            }
        })
        .catch(error => {
            console.log(JSON.stringify(error));
            return null;
        });
    return reponse;
}
