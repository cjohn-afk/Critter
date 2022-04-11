var likeAPI = '/API/like'
var postAPI = '/API/post'

function postIDObj(postID) {
    return { id: postID }
}

function postObj(text) {
    return { text: text }
}

function updateState(API_URL, method, content) {
    return fetch(API_URL, {
            method: method, 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(content)
        });
}

function like(postID) {
    updateState(likeAPI, 'POST', postIDObj(postID))
    .then( response => {
        if (response.status == 200) {
            let post = document.getElementById("post_" + postID)
            let likeButton = post.getElementsByClassName("like_icon")[0]
            let likeNum = post.getElementsByClassName("num_likes")[0]

            if (likeButton.innerHTML == "favorite") {
                likeButton.innerHTML += "_border"
                likeNum.innerHTML = parseInt(likeNum.innerHTML) - 1
            } else {
                likeButton.innerHTML = "favorite"
                likeNum.innerHTML = parseInt(likeNum.innerHTML) + 1
            }
        }
    })
}

function post(text) {
    updateState(postAPI, 'POST', postObj(text))
}

function deletePost(postID) {
    updateState(postAPI, 'POST', postIDObj(postID))
    .then( response => {
        if (response.status == 200){
            let post = document.getElementById("post_" + postID)
            post.classList += " hidden"
            setTimeout(function(){
                post.remove()
            }, 1000);
        }
    })
}