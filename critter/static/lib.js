var likeAPI = '/API/like'
var postAPI = '/API/post'

function postIDObj(postID) {
    return { id: postID }
}

function postOBJ(text) {
    return { text: text }
}

function updateState(API_URL, method, content) {
    fetch(API_URL,{
        method: method,
        headers:{
        'Content-Type':'application/json'
        },
        body: JSON.stringify(content)
    })
}

function addLike(postID) {
    updateState(likeAPI, 'POST', postIDObj(postID))
}

function addPost(text) {
    updateState(postAPI, 'POST', postObj(text))
}