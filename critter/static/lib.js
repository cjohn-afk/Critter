var likeAPI = '/API/like'
var postAPI = '/API/post'

function postIDObj(postID) {
    return { id: postID }
}

function postOBJ(text) {
    return { text: text }
}

function updateState(API_URL, method, content) {
    const fetchPromise = fetch(API_URL, {
            method: method, 
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(content)
        });

        fetchPromise.then( response => {
            if (response.status == 200) {
                let post = document.getElementById("post_" + content.id)
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

function addLike(postID) {
    updateState(likeAPI, 'POST', postIDObj(postID))
}

function addPost(text) {
    updateState(postAPI, 'POST', postObj(text))
}