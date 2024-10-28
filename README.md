# E-Commerce Customer Churn Prediction
![image](https://github.com/user-attachments/assets/b3bdd1a4-fc9c-4196-946b-7fb1faacb4dc)

## 1. Introduction
- Predicting customer churn is a crucial task for businesses aiming to retain their customers and reduce turnover rates. The churn prediction problem involves identifying customers who are likely to stop using a service or product within a certain period. To solve this, companies analyze historical customer data, including demographic information, transaction histories, service usage patterns, and customer interactions. Machine learning algorithms, such as decision trees, logistic regression, SVM, XGBoost, are commonly applied to this data to build predictive models and feature engineering was applied to import model efficiency. By accurately identifying potential churners, businesses can take proactive measures, such as personalized marketing strategies or customer support interventions, to retain valuable customers and improve overall customer satisfaction. As the result, XGboost achieves the biggest accurancy, F1-score, Recall. \
Demo churn prediction app: https://drive.google.com/file/d/1Gp03_-Lh2TzCc1M2xCFMxZf1u38I_FbW/view?usp=sharing

![image](https://github.com/user-attachments/assets/aadb7021-0994-4e42-ba1b-0fcd15ad125e)

## 2. Dataset source
- From kaggle, link: https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/data
## 3. Cleaning data
After quantity statistics, I had 'Tenure': 264 missing value, 'WarehouseToHome': 251 missing value, 'HourSpendOnApp':	255 missing value, 'OrderAmountHikeFromlastYear':	265 missing value, 'CouponUsed':	256 missing value, 'OrderCount':	258 missing value, 'DaySinceLastOrder':	307 missing value. All variable above I filled median value in every ariable, respectively.
## 4. EDA
- Phân bố nhãn của Churn cho thấy tỉ lệ khách hàng rời bỏ doanh nghiệp chiếm 16.8% trong bộ dữ liệu -> Bộ dữ liệu mất cân bằng.
![image](https://github.com/user-attachments/assets/23ef5926-6a3a-43bc-9825-3bde47c83eb5)
- Biểu đồ box-plot cho các biến có kiểu dữ liệu số để thể hiện sự phân bố của các điểm dữ liệu và có thể nhận dạng giá trị ngoại lai (outliers)
![image](https://github.com/user-attachments/assets/e7deb0e2-0644-4999-ae3d-af211f11813e)
![image](https://github.com/user-attachments/assets/f3c048aa-f2e7-47c7-9ff5-0fc9d34721e6)
- Hình ảnh thể hiện tầng suất xuất hiện của thể loại trong biến phân loại -> có thể thấy được khách hàng có xu hướng dùng theo 1 thể loại cụ thể chiếm ưu thế hơn. Cụ thể trong hình thứ 1, điện thoại (phone) được dùng để mua hàng gấp đôi máy tính (computer). Ở các hình tiếp theo , khách hàng ưu tiên trả tiền bằng Thẻ ghi nợ (Debit card), đa số các lượt mua hàng là khách hàng nam -> đưa ra chiến lược phù hợp thu hút khách hàng nam dựa trên tính cách và sở thích của họ. Chính vì có nhiều khách hàng nam mua hàng nên sản phẩm về Mobile và Laptop & Accessory bán chạy hơn hẳn các thể loại hàng hóa khác trong biểu đồ thứ 4. Hơn nữa, khách hàng đã kết hôn có xu hướng mua hàng nhiều hơn để nâng cao chất lượng cuộc sống gia đình -> nhắm hoàn toàn mục tiêu vào hộ gia đình hoặc cung cấp khác loại mặt hàng khác nhằm thực hiện đa dạng sản phẩm đến mọi người trong xã hội cũng như mở rộng doanh nghiệp.
![image](https://github.com/user-attachments/assets/9bc9913d-a0c9-4247-8e92-83ab85bd6c37)
- Tenure là 1 biến thể hiện thời gian gắn bó của khách hàng đối với doanh ngiệp. Có thể thấy là đa số khách hàng hiện tại gắn bó với doanh nghiệp được khoảng dưới 10 năm là cao nhất và giảm dần theo các khoảng thời gian tiếp theo. Để nâng cao sự gắn bó của khách hàng với thời gian lâu hơn thì cần phát hiện những khách hàng muốn rời bỏ doanh nghiệp để áp dụng những chính sách ưu đãi giữ chân khách hàng.
![image](https://github.com/user-attachments/assets/42b52524-c1d4-4926-b04b-1572e388377f)
- Phân bố của khách hàng churn theo từng biến.
![image](https://github.com/user-attachments/assets/796987ad-6746-4e25-bc56-11e0a63de9eb)
![image](https://github.com/user-attachments/assets/dcfd9e10-7dce-44df-a81a-48b1c119d367)
![image](https://github.com/user-attachments/assets/f65651c1-0cad-4a1b-add5-f37dab34d165)
![image](https://github.com/user-attachments/assets/1bb86acf-bb04-46c2-9d43-fecb44e97de1)




