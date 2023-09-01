document.addEventListener("DOMContentLoaded", function () {
    const hashtagForm = document.getElementById("hashtagForm");
    const hashtagsResult = document.getElementById("hashtagsResult");

    hashtagForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const keyword = document.getElementById("keyword").value;
        const numHashtags = document.getElementById("numHashtags").value;

        fetch(`/generate?keyword=${keyword}&num_hashtags=${numHashtags}`)
            .then((response) => response.json())
            .then((data) => {
                hashtagsResult.innerHTML = "";
                if (data.length > 0) {
                    data.forEach((hashtag, index) => {
                        const hashtagElement = document.createElement("p");
                        hashtagElement.textContent = `${index + 1}. ${hashtag}`;
                        hashtagsResult.appendChild(hashtagElement);
                    });
                } else {
                    hashtagsResult.textContent = "No hashtags found.";
                }
            })
            .catch((error) => {
                console.error("An error occurred:", error);
                hashtagsResult.textContent = "Error fetching hashtags.";
            });
    });
});
