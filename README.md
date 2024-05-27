# Flask
![Flask](https://github.com/jisuhaha/saas/assets/152825532/160aacc0-c4c3-48c9-983d-0d4d0c8175ad)

Flask 
Python으로 작성된 마이크로 웹 프레임워크

### 선정 이유
- 교육 기간 내 구성원 모두 학습했던 경험
- 쉬운 학습 곡선 (Flask는 간단한 API와 명확한 문서를 제공하여, Python 초보자도 쉽게 학습 및 사용 가능. 또한, Flask 애플리케이션의 구조가 직관적.)
- 유연한 템플릿엔진(Jinja2), SQL Alchemy등의 플러그인 및 커뮤니티 지원
  
# ArgoCD
![Argo CD](https://github.com/jisuhaha/saas/assets/152825532/260123dd-a770-4d94-8e69-af8afebf2157)
ArgoCD는 GitOps 원칙을 따름Kubernetes 환경에서 지속적 배포(Continuous Deployment)를 자동화하고 관리하는 데 특화된 도구

### 선정 이유
- Kubernetes 리소스의 배포와 관리를 자동화.
- 수작업 배포에서 발생할 수 있는 실수를 줄이고, 배포 프로세스 표준화 가능.
- 문제 발생 시 이전 안정된 상태로 자동 롤백할 수 있어, 신속한 문제 해결이 가능.
- 강력한 시각화 및 관리 UI

### WorkFlow File CICD.yaml

GitOps 원칙
애플리케이션의 선언적 정의를 Git 저장소에 보관하고, Git을 단일 진실의 출처(single source of truth)로 사용하는 방식.

# MariaDB
![mariadb_logo_icon_168996](https://github.com/jisuhaha/saas/assets/152825532/83df83f1-5ca1-4a4b-9195-aabbd7430e01)
MariaDB는 무료 오픈소스 관계형 데이터베이스 관리 시스템(RDBMS)

### 선정 이유
- 교육 기간 내 구성원 모두 학습했던 경험이 있음
- AWS 서비스중 데이터베이서 서비스 RDS에 지원중인 엔진 및 RDBMS특성 상 데이터의 무결성을 보장



# NGINX
#![NGINX](https://github.com/jisuhaha/saas/assets/152825532/427105e5-6eb0-401e-9841-1a68c95118ff)
웹 서버 소프트웨어
### 선정 이유
- 이전 프로젝트에서 웹서버 소프트웨어로 Apachce 웹서버를 사용, 많이 사용되고 있는 Nginx의 사용 경험을 쌓는 것이 필요하다고 판단.
- Nginx는 이벤트 기반 아키텍처를 사용하여 높은 동시성 처리를 효율적으로 수행. 이는 많은 수의 동시 연결을 처리하는 데 유리함.
  반면, Apache는 기본적으로 프로세스 또는 스레드 기반 모델을 사용하므로, 동시성 처리가 증가할 때 성능 저하가 발생할 수 있음.


--------------------------
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

