# source 

### 게시판 관련 서비스
#### service: Bunisess Logic집합
 - boardService.py : 게시글 등록 / 조회 / 수정 / 삭제, 게시글 목록보기 
 - cronService.py : 축제정보 수집 일 배치
 - loginService.py : 포털로그인, oauth login callback redirection Check, Toekn 발급
 - mainPageService.py : Utility형식의 함수들 정의
 - myPageService.py : 마이페이지
 - recommandResult.py : 여행지 추천
 - registryService.py : 회원가입
#### Static : css, fonts, Image, JavaScript 
#### templates : HTML 
 - board.html, boardCreate.html, boardData.html, boardEdit.html  : 게시글목록 조회, 게시글 생성, 게시글 조회 게시글 생성
 - index.html : 메인 페이지
 - login.html : 로그인 페이지
 - myPage.html : 마이 페이지
 - recommand.html : 추천 페이지
 - recommandResult.html : 추천 결과 페이지
 - registry.html : 회원가입 페이지
#### config.py : 설정 관련
 - db connection Information
#### database.py : SQL Alchemy Database access CRUD 함수 정의
#### init.py : sql Alchemy 설정
#### models.py : DB 모델 Class
#### project.py : Route 설정

