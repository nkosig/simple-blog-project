import { httpClient, baseUrl } from '../utils/httpClient';

export async function getPostBySlug() {
    const rsp = await httpClient.get(`${baseUrl}/posts`)
        .then(response => {
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
    return rsp;
}

export async function getPostById(topicId, postId) {
    console.log()
    const rsp = await httpClient.get(`${baseUrl}/topics/${topicId}/posts/${postId}`)
        .then(response => {
            if (response.data && response.data.length > 0) {
                return response.data;
            } else {
                return null;
            }
        })
        .catch(error => {
            console.log(JSON.stringify(error));
            return null;
        });
    return rsp;
}

