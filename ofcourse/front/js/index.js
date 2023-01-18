// console.log("index.js used!")

//* 가로 스크롤 구현

//* 요소, 사이즈
const list = document.querySelector(".list-card > .skill-list ul");
const listScrollWith = list.scrollWidth;
const listClientlWith = list.clientWidth;

//* 이벤트마다 갱신할 값
let startX = 0;
let nowX = 0;
let endX = 0;
let listX = 0;

console.log(list, listScrollWith, listClientlWith);

//* 이벤트 헨들러 선언
// 스크롤 시작 이벤트
const onScrollStart = (e) => {
    console.log("scroll start");
    startX = getClientX(e);
    window.addEventListener("mousemove", onScrollMove);
    window.addEventListener("mouseup", onScrollEnd);
    window.addEventListener("touchmove", onScrollMove);
    window.addEventListener("touchend", onScrollEnd);
};
// 스크롤 진행 이벤트
const onScrollMove = (e) => {
    console.log("scroll move");
    nowX = getClientX(e);
    setTranslateX(listX - nowX - startX);
};
const onScrollEnd = (e) => {
    console.log("scroll ends");
};
const onClick = (e) => {
    console.log("scroll click");
};

//* 유틸 함수 정의 - 코드에서 재사용되는 부분
const getClientX = (e) => {
    const isTouches = e.touches ? true : false;
    return isTouches ? e.touches[0].clientX : e.clientX;
};
const getTranslateX = () => {
    console.log("get");
    return parseInt(getComputedStyle(list).transform.split(/[^\-0-9]+/g)[5]);
};
const setTranslateX = (x) => {
    console.log("setTranslate");
    list.style.tranform = `translateX(${x}px)`;
};

// 이벤트 바인딩
const bindEvents = () => {
    list.addEventListener("mousedown", onScrollStart);
    list.addEventListener("touchStart", onScrollStart);
    list.addEventListener("click", onClick);
};
bindEvents();
