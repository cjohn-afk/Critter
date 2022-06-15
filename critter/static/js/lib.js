var likeAPI = '/API/like'
var postAPI = '/API/post'
var followAPI = '/API/follow'

function IDObj(postID) {
    return { id: postID }
}

function textObj(text) {
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
    updateState(likeAPI, 'POST', IDObj(postID))
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

function post() {
    text = document.getElementById("text").value
    updateState(postAPI, 'POST', textObj(text))
    .then( response => {
        
    })
}

function deletePost(postID) {
    updateState(postAPI, 'POST', IDObj(postID))
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

function follow(userID) {
    updateState(followAPI, 'POST', IDObj(userID))
    .then( response => {
        if (response.status == 200) {
            let profile = document.getElementById("profile")
            let followButton = profile.getElementsByClassName("follow_icon")[0]

            if (followButton.innerHTML == "person_add_alt") {
                followButton.innerHTML += "_1"
            } else {
                followButton.innerHTML = "person_add_alt"
            }
        }
    })
}