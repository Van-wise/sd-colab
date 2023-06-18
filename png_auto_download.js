(async () => {
  const delayGenerateButton = async () => {
    return new Promise((resolve) => {
      const shadowRoot = document.querySelector("gradio-app");
      const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
          if (
            mutation.addedNodes.length &&
            mutation.addedNodes[0].id === "txt2img_generate"
          ) {
            observer.disconnect();
            resolve();
          }
        }
      });
      observer.observe(shadowRoot, { childList: true, subtree: true });
    });
  };

  const downloadImage = (url, fileName) => {
    fetch(url)
      .then((response) => response.blob())
      .then((blob) => {
        const a = document.createElement("a");
        const url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
      });
  };

  const downloadGeneratedImages = async (buttonId, galleryId) => {
    const button = document.querySelector(buttonId);
    let state = "pending";

    button.onclick = async () => {
      const rootNode = document.querySelector(galleryId);
      const parentNode = rootNode.querySelector(`${galleryId} > div.grid-wrap > div`);

      if (state === "pending") {
        state = "fulfilled";
        await observeAndDownloadImages(rootNode, state);
      } else {
        observeAndDownloadImages(parentNode, state);
      }
    };
  };

  const observeAndDownloadImages = (parentNode, state) => {
    return new Promise((resolve) => {
      const observer = new MutationObserver((mutations) => {
        try {
          for (const mutation of mutations) {
            if (
              mutation.target.localName === "img" ||
              (mutation.addedNodes[0] && mutation.addedNodes[0].localName === "img")
            ) {
              observer.disconnect();
              downloadImagesFromNode(parentNode);
              throw "Force exit loop";
            }
          }
        } catch (out) {
          resolve();
        }
      });
      observer.observe(parentNode, { attributes: true, childList: true, subtree: true });
    });
  };

  const downloadImagesFromNode = (parentNode) => {
    const imageNodes = parentNode.querySelectorAll(".thumbnail-item > img");
    imageNodes.forEach((imgNode) => {
      const nameArr = imgNode.src.split("/");
      const name = decodeURIComponent(nameArr[nameArr.length - 1]);
      downloadImage(imgNode.src, name);
    });
  };

  const initDownload = async () => {
    await delayGenerateButton();
    await downloadGeneratedImages("#txt2img_generate", "#txt2img_gallery");
    await downloadGeneratedImages("#img2img_generate", "#img2img_gallery");
    await downloadGeneratedImages("#extras_generate", "#extras_gallery");
  };

  document.addEventListener("DOMContentLoaded", initDownload);
})();
