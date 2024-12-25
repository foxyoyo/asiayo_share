
# 試想臨時有一活動網頁專案將於近日推出，預期推廣期間訪客流量會是平日常態之百倍（或更多）請簡易描述你/妳將如何確保服務能在推廣期間正常運作？考量的細節是什麼？
```plantext
Ans : 
1:  先推估出可能需要的resource:
      可依據平日制定的 SLI / SLO metrics 標準，大概嘗試推估推廣期間的可能流量與所需resource 
      i.e:  假設Prod環境是在K8S （EKS），平常期待尖峰時間 http request 希望平均 response time < 1.5ms ，會需要 api pods 數量40個才能滿足時，
      去推估活動期間，可能需要多少pod，跟多少worker nodes來應對。

2:  按照推估的量，在活動來之前，先把AutoScaleingGroup / Pod replicas 先設定好，等待traffic （i.e: 活動期間可能會有 pod replica = 120個 ，worker-nodes 先準備好 ）
      
3:  其他：
    3.1 :  如果有突然流量，或超乎預期的流量，可設定HPA 或 整合 KEDA應用等方式 。
    3.2 :  除了 api , frontend 這些pods 的AutoScaling 外，其他架構上components 是否能應對？ i.e : Redis memory 提前加大， RDS spec 是否需暫時升級。
    3.3 :  需要關注的monitor metrics ， redis:mem , swap .  http avg response time 等等，RDS iops ,slow log 等等。 

4: Change EKS ASG Worker node cronjob :
   docker buildx build --platform=linux/amd64  -f ./Dockerfile -t foxyo/cronjob-chg-asg:latest .
   modiy cronjob_for_asg_worker.yaml for ENV: MaxNode , MinNode, schedule time 

```

# 試想有一個 API 伺服器集群，背後由多台機器組成，此時服務監控系統發現其中一台回應時間經常逾時，僅有此機器異常，請簡易描述你/妳將會如何進行問題排查？考量的細節是什麼？
```plantext
Ans:
1: 會先觀察該機器那段期間CPU / mem / disk io / network 等metrics 是否在異常期間也同步升高，在進一步該台機器上除了API服務還有什麼在佔用resource
   如果是linux OS ，可以運用 atop , htop, lsop , top, ps -ef . strace 等等指令進一步追查。
   如果是K8S Worker node ，需仰賴node exporter , metrics , prometheus , alertmanager 等等，取得pod 運用resource 狀態，看是否有pod 彼此之間race condition 
```

# 試想有一項目運行於 AWS EC2 機器之上，已確認該服務仍然正常運行中，但由於不明原因導致無法再次透過 SSH 登入確認狀態（已確認排除並非網路異常，亦非防火牆阻擋所導致）。請簡易描述你/妳將如何排查問題，並且讓服務恢復正常運作？考量的細節是什麼？如果可以，請試著回答造成無法登入的可能的肇因為何？
```plantext
Ans: 
AWS EC2 有一個可以透過 web console login (模擬本機登入)，看能不能登入，並且開始查詢 ssh 的log , system log 看是否有相關error log 指出原因. 
1: 是否有enable Selinux ? 可以暫時關閉驗證看看。
2: ssh 本身有很多整合其他認證方式，驗證方式的設定（ i.e: pam module的設定方式 ），看是不是那段設定有改變。
如果log看不出，網路/ firewall 又排除，僅與ssh service 相關，可以暫時 restore sshd 預設設定檔，來快速釐清測試，問題是不是在sshd config 有相關
```

# 試想已有一組 ELK/EFK 日誌服務集群，而今日有一新服務上線並且串接日誌紀錄，讓開發者能夠透過 Kibana 進行線上錯誤排查，你/妳會如何將日誌檔內容串接至 ELK/EFK 系統？考量的細節是什麼？
```plantext

    1: Application 的 log 的format ，建議是json , 如此一來可直接使用i.e: fluentbit的 json parser , 不需要去自行寫 pattern parser 或 ingest pipeline.
    2: 是否需要作index 分類的動作，譬如不同 input ，filter ，re-write tag 等等，分流到不同output . 
    3: RD , application 有沒有規劃特定 trace id 欄位，方便在servie mesh 環境中排查 不同服務互相呼叫的log . 

```