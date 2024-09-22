fetch("/api/main/getHomepageMessage")
  .then((resp) => resp.json())
  .then((data) => {
    const el = document.querySelector(".homepage-message");
    el.innerText = data.message;
  });
