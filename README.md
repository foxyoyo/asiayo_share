# asiayo_share
# Question 1:  請以任意語言/形式撰寫一段腳本，找出“words.txt” 檔案內容中重複次數最多的單字 （大小寫將忽略不計。舉例來說：the/The 將會被視為相同單字）
- 參數說明 ：
```
command : echo "$document" | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr ' ' '\n' | grep -v '^$' | sort | uniq -c | sort -nr | head -n 1

tr '[:upper:]' '[:lower:]': 將所有字統一轉成小寫格式。
tr -d '[:punct:]': 移除標點符號
tr ' ' '\n': 將每個單字分行。
grep -v '^$': 移除空行
sort: 對單字進行排序，為後續 uniq -c 提供條件。
uniq -c: 計算每個單字出現次數。
sort -nr: 排序由高到低。
head -n 1: 第一個則為次數最多的字。
```

- How to use:
```

➜  Question1 git:(master) ✗ ls
count_words.sh words.txt      words2.txt

chmod +x ./count_words.sh

# 統計輸入為words.txt 與words2.txt
➜  Question1 git:(master) ✗ ./count_words.sh -f ./words2.txt
  18 the
➜  Question1 git:(master) ✗ ./count_words.sh -f ./words.txt
   4 twinkle

# 如果沒有指定 input file path:
 ➜  Question1 git:(master) ✗ ./count_words.sh
Please specific your file path

i.e: Usage: count_words.sh -f ./words.txt
	 -f: Your file Path

```

# asiayo_share
# Question 2:  Terraform EKS + K8S
- Terraform Build EKS ：
```
terraform init
terrafrom plan

# 模擬結果：
terraform plan -out tf.plan
terraform show -no-color tf.plan > tfplan.txt

```

- K8S Yaml ：
```
mysql-sts.yaml
asiayo-svc.yaml

```