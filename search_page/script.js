document.addEventListener('DOMContentLoaded', function () {
    // const itemsPerPage = 18; 
    const resultContent = document.getElementById('resultContent');
    const totalPageElement = document.getElementById('totalPage');
    const currentPageElement = document.getElementById('currentPage');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    const videoSources = [
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        './assets/hêh.mp4',
        './assets/3205442632339.mp4',
        './assets/test.mp4',
        
    ];

    const totalVideo = videoSources.length;
    const totalPage = Math.ceil(totalVideo / 18); 


    totalPageElement.textContent = totalPage;

    // Animation chuyển trang
    resultContent.classList.add('fade-out');

    function showPage(pageNumber) {
        
        resultContent.innerHTML = '';

        // Xác định phạm vi video cho trang hiện tại
        const start = (pageNumber - 1) * 18;
        const end = Math.min(start + 18, totalVideo);

        
        for (let i = start; i < end; i++) {
            const videoItem = document.createElement('div');
            videoItem.className = 'result-item';
            videoItem.innerHTML = `
                <i class="fa-regular fa-heart"></i>
                <video src="${videoSources[i]}" muted></video> 
            `;
            resultContent.appendChild(videoItem);
        }

       
        for (let i = end; i < start + 18; i++) {
            const emptyItem = document.createElement('div');
            emptyItem.className = 'empty-item';
            resultContent.appendChild(emptyItem);
        }

        
        currentPageElement.textContent = pageNumber;  

        prevBtn.disabled = (pageNumber === 1);
        nextBtn.disabled = (pageNumber === totalPage);
    }

    
    nextBtn.addEventListener('click', function () {
        if (currentPage < totalPage) {
            currentPage++;
            showPage(currentPage);
        }
    });

    
    prevBtn.addEventListener('click', function () {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    
    let currentPage = 1;
    showPage(currentPage);

    
    const overlay = document.getElementById('videoOverlay');
    const popupVideo = document.getElementById('popupVideo');
    const closePopup = document.getElementById('closePopup');

    resultContent.addEventListener('click', function (event) {
        const target = event.target;

        if (target.tagName === 'I' && target.classList.contains('fa-heart')) {
            // Nhấp vào trái tim
            if (target.classList.contains('fa-regular')) {
                target.classList.remove('fa-regular');
                target.classList.add('fa-solid');
            } else {
                target.classList.remove('fa-solid');
                target.classList.add('fa-regular');
            }
            event.stopPropagation(); // Không cho nó lan truyền ra thẻ to
        } else if (target.closest('.result-item')) {
            // 
            const videoSource = target.closest('.result-item').querySelector('video').getAttribute('src');
            popupVideo.setAttribute('src', videoSource);
            overlay.style.display = 'flex';
        }
    });

   
    closePopup.addEventListener('click', function () {
        overlay.style.display = 'none';
        popupVideo.pause();
        popupVideo.removeAttribute('src');
    });

    
    overlay.addEventListener('click', function (e) {
        if (e.target === overlay) {
            overlay.style.display = 'none';
            popupVideo.pause();
            popupVideo.removeAttribute('src');
        }
    });

    // Idol bảo là không để delay
    let hoverTimeout;
    resultContent.addEventListener('mouseover', function (event) {
        const target = event.target;

        if (target.tagName === 'VIDEO') {
            clearTimeout(hoverTimeout);
            hoverTimeout = setTimeout(() => {
                target.play();
            });
        }
    }, true);

    resultContent.addEventListener('mouseout', function (event) {
        const target = event.target;

        if (target.tagName === 'VIDEO') {
            clearTimeout(hoverTimeout);
            target.pause();
            target.currentTime = 0; 
        }
    }, true);

    resultContent.addEventListener('mouseover', function (event) {
        const target = event.target;

        if (target.tagName === 'I' && target.classList.contains('fa-heart')) {
            clearTimeout(hoverTimeout); 
        }  
    }, true);
});
