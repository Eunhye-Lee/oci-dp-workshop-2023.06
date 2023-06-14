# S02 - Data Replication 실습
### 1. ATP -> ADW 간 데이터 동기화
#### *Source Database 설정
  1. 좌측상단 메뉴 버튼을 클릭하고, Oracle Database > Autonomous Transaction Processing을 클릭합니다. 
  2. ATP database를 클릭하고, Database Actions 버튼을 클릭합니다.
  3. OGG Configuration을 위한 GGADMIN 유저를 Unlock합니다. GGADMIN 유저 옆에 버튼을 누르고 편집을 클릭합니다. 해당 유저를 위한 비밀번호를 ‘WElcome123__’로 설정하고 ‘계정이 잠겨있습니다’를 해제 하여 Unlock 해줍니다. ‘변경사항 적용’ 버튼을 클릭합니다.
  4. 다시 앞 화면으로 돌아와서 SQL 메뉴를 클릭합니다. 
  5. ```alter pluggable database add supplemental log data;``` 설정하여 소스데이터 변경을 완료합니다.
  
#### *Target Database 설정
  1. 좌측상단 메뉴 버튼을 클릭하고, Oracle Database > Autonomous Data Warehouse를 클릭합니다. 
  2. Create Autonomous Database를 클릭합니다.
  3. ADW정보를 입력합니다. Create Autonomous Database 버튼을 클릭합니다.
  4. 생성이 완료 되었으면, Database actions를 클릭합니다.  
  5. 관리 > 데이터베이스 사용자를 클릭합니다.
  6. OGG Configuration을 위한 GGADMIN 유저를 Unlock합니다. GGADMIN 유저 옆에 버튼을 누르고 편집을 클릭합니다. 해당 유저를 위한 비밀번호를 ‘WElcome123__’로 설정하고 ‘계정이 잠겨있습니다’를 해제 하여 Unlock 해줍니다.
  7. 유저까지 구성이 완료 되었으면, 데이터 integration을 위해 Target Database의 테이블을 생성합니다. 좌측 상단의 메뉴를 클릭하여, 개발 > SQL을 클릭합니다.  
  8. DDL을 수행합니다. 
  ```
  CREATE TABLE livelabs (
  id NUMBER PRIMARY KEY,
  title VARCHAR2(1024),
  title_ko VARCHAR2(1024),
  description VARCHAR2(4096),
  description_ko VARCHAR2(4096),
  url VARCHAR2(1024),
  type VARCHAR2(30),
  duration VARCHAR2(30),
  duration_ko VARCHAR2(30),
  crawled_date DATE,
  oci_products VARCHAR2(2048),
  key_phrase VARCHAR2(2048)
);
```

#### *OCI-GG 설정
  1. 좌측 상단 메뉴에서 Oracle Database > Goldengate를 클릭합니다.
  2. 인스턴스 생성을 위해 Create Deployment를 클릭합니다.
  3. 인스턴스 이름, OCPU, Subnet 및 라이선스 타입을 선택합니다. ‘Show advanced options’를 클릭하여, Enable GoldenGate console public access을 클릭합니다. (이번 실습에서는, 편의상 Public Subnet을 활용하여 구성합니다.) 아래와 화면 같이 작성한 후에, Next 버튼을 클릭합니다. 


 


