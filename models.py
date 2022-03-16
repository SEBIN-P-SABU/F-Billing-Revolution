import mysql.connector


fbilldb = mysql.connector.connect(
     host="localhost", user="root", password="", database="fbilldb", port="3306"
 )
fbcursor = fbilldb.cursor()
# fbcursor.execute("""
#                  create table Company(
#                      companyid int AUTO_INCREMENT, 
#                      name varchar(255),
#                      address varchar(255),
#                      email varchar(255),
# 		             salestaxno varchar(255),
#                      currency varchar(255),
#                      currencysign int,
# 		             currsignplace varchar(255),
#                      decimalseperator varchar(255),
#                      excurrency varchar(255),
#                      dateformat varchar(255),
#                      exdate varchar(255),
#                      taxtype varchar(255),
#                      printtaxornot varchar(255),
#                      taxname varchar(255),
#                      taxrate FLOAT,
#                      image BLOB,
#                      printimageornot varchar(255),
#                      PRIMARY KEY(companyid))
#                 """)
# fbcursor.execute("""
#                  create table Productservice(
#                      Productserviceid int AUTO_INCREMENT,
#                      companyid int,
#                      sku varchar(255),
#                      category varchar(255),
#                      name varchar(255),
# 		             description varchar(255),
#                      status varchar(255),
#                      unitprice int,
# 		             peices varchar(255),
#                      cost int,
#                      taxable varchar(255),
#                      priceminuscost int,
#                      serviceornot varchar(255),
#                      stock int,
#                      stocklimit int,
#                      warehouse varchar(255),
#                      privatenote varchar(255),
#                      image LONGBLOB,
#                      PRIMARY KEY(Productserviceid),
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)
# fbcursor.execute("""
#                  create table Customer(
#                      customerid int AUTO_INCREMENT,
#                      companyid int,
#                      category varchar(255),
#                      status varchar(255),
#                      businessname varchar(255),
#                      businessaddress varchar(255),
#                      shipname varchar(255),
#                      shipaddress varchar(255),
#                      contactperson varchar(255),
#                      cpemail varchar(255),
#                      cptelno varchar(255),
#                      cpfax varchar(255),
#                      cpmobileforsms varchar(255),
#                      shipcontactperson varchar(255),
#                      shipcpemail varchar(255),
#                      shipcptelno varchar(255),
#                      shipcpfax varchar(255),
                 
#                      taxexempt varchar(255),
#                      specifictax1 int,
#                      discount int,
                 
#                      country varchar(255),
#                      city varchar(255),
#                      customertype varchar(255),
#                      notes varchar(255),
                 
#                      PRIMARY KEY(customerid),
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)
# fbcursor.execute("""
#                  create table estimate(
#                      estimateid int AUTO_INCREMENT,
#                      companyid int,
#                      estimate_number varchar(255),
#                      estimatedate varchar(255),
#                      duedate varchar(255),
#                      status varchar(255),
#                      emailon varchar(255),
#                      printon varchar(255),
#                      smson varchar(255),
#                      estimatetot int,
#                      totpaid int,
#                      balance int,
#                      extracostname varchar(255),
#                      extracost int,
#                      template varchar(255),
#                      salesper varchar(255),
#                      discourate int,
#                      tax1 int,
#                      category varchar(255),
#                      customerid int,
#                      Productserviceid int,
#                      PRIMARY KEY(estimateid),
#                      FOREIGN KEY (customerid) REFERENCES Customer (customerid) ON DELETE CASCADE,
#                      FOREIGN KEY (Productserviceid) REFERENCES Productservice (Productserviceid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)   

# fbcursor.execute("""
#                  create table invoice(
#                      invoiceid int AUTO_INCREMENT,
#                      invoive_number varchar(255),
#                      invodate DATE,
#                      duedate DATE,
#                      status varchar(255),
#                      emailon varchar(255),
#                      printon varchar(255),
#                      smson varchar(255),
#                      invoicetot int,
#                      totpaid int,
#                      balance int,
#                      extracostname varchar(255),
#                      extracost int,
#                      template varchar(255),
#                      salesper varchar(255),
#                      discourate int,
#                      tax1 int,
#                      category varchar(255),
#                      businessname varchar(255),
#                      businessaddress varchar(255),
#                      shipname varchar(255),
#                      shipaddress varchar(255),
#                      cpemail varchar(255),
#                      cpmobileforsms varchar(255),
#                      companyid int,                     
#                      customerid int,
#                      Productserviceid int,
#                      PRIMARY KEY(invoiceid),
#                      FOREIGN KEY (customerid) REFERENCES Customer (customerid) ON DELETE CASCADE,
#                      FOREIGN KEY (Productserviceid) REFERENCES Productservice (Productserviceid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """) 
# fbcursor.execute("""
#                  create table Expenses(
#                      expensesid int AUTO_INCREMENT,
#                      customerid int,
#                      companyid int,
#                      expense_amount int,
#                      date DATE,
#                      vendor varchar(255),
#                      catagory varchar(255),
#                      description varchar(255),
#                      staff_members varchar(255),
#                      taxable varchar(255),
#                      customer varchar(255),
#                      image BLOB,
#                      notes varchar(255),
#                      rebillable varchar(255),
#                      invoiced varchar(255),
#                      id_sku int,
#                      rebill_amount int,
#                      PRIMARY KEY(expensesid),
#                      FOREIGN KEY (customerid) REFERENCES Customer (customerid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)
# fbcursor.execute("""
#                  create table porder(
#                      porderid int AUTO_INCREMENT,
#                      companyid int, 
#                      porderdate varchar(255),
#                      duedate varchar(255),
#                      customname varchar(255),
#                      status varchar(255),
#                      emailon varchar(255),
#                      printon varchar(255),
#                      smson varchar(255),
#                      ordertot int,
#                      total int,
#                      extracostname varchar(255),
#                      extracost int,
#                      template varchar(255),
#                      salesper varchar(255),
#                      discourate int,
#                      tax1 int,
#                      category varchar(255),
#                      Productserviceid int,
#                      customerid int,
#                      PRIMARY KEY(porderid),
#                      FOREIGN KEY (customerid) REFERENCES Customer (customerid) ON DELETE CASCADE,
#                      FOREIGN KEY (Productserviceid) REFERENCES Productservice (Productserviceid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)
# fbcursor.execute("""
#                  create table Recurring(
#                      recurringid int AUTO_INCREMENT,
#                      companyid int,
#                      recurring_period int,
#                      next_invoice date,
#                      stop_recurring date,
#                      customerid int,
#                      PRIMARY KEY(recurringid),
#                      FOREIGN KEY (customerid) REFERENCES Customer (customerid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)     
# fbcursor.execute("""
#                  create table SMS(
#                      smsid int AUTO_INCREMENT,
#                      companyid int,
#                      sms_type varchar(255),
#                      sms_text varchar(255),
#                      customerid int,
#                      PRIMARY KEY(smsid),
#                      FOREIGN KEY (customerid) REFERENCES Customer (customerid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)
# fbcursor.execute("""
#                  create table SMS_Account(
#                      smsaccountid int AUTO_INCREMENT,
#                      companyid int,
#                      username varchar(255),
#                      api_secret varchar(255),
#                      route varchar(255),
#                      api_key varchar(255),
#                      smsid int,
                 
#                      PRIMARY KEY(smsaccountid),
#                      FOREIGN KEY (smsid) REFERENCES SMS (smsid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)    
# fbcursor.execute("""
#                  create table Invoice_Private_Notes(
#                      invoicepvtnoteid int AUTO_INCREMENT,
#                      companyid int,
#                      private_notes varchar(255),
                 
#                      PRIMARY KEY(invoicepvtnoteid),
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
                 
#                 """)    
# fbcursor.execute("""
#                  create table Comments(
#                      commentid int AUTO_INCREMENT,
#                      companyid int,
#                      comment varchar(255),
                 
#                      PRIMARY KEY(commentid),
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """) 
# fbcursor.execute("""
#                  create table Documents(
#                      documentid int AUTO_INCREMENT,
#                      companyid int,
#                      documents varchar(500),
                 
#                      PRIMARY KEY(documentid),
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """) 
# fbcursor.execute("""
#                  create table Markinvoice(
#                      paymentid int AUTO_INCREMENT,
#                      companyid int,
#                      invoice_balance varchar(255),
#                      payment_date date,
#                      paid_by varchar(255),
#                      description varchar(255),
#                      full_paid varchar(255),
#                      payment_receipt varchar(255),
#                      attach_invoice varchar(255),
#                      PRIMARY KEY(paymentid),
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)
# fbcursor.execute("""
#                  create table Orders(
              
#                      orderid int AUTO_INCREMENT, 
#                      order_date DATE,
#                      due_date DATE,
#                      businessname varchar(255),
# 		             status varchar(255),
#                      emailed_on varchar(255),
#                      printed_on varchar(255),
# 		             sms_on varchar(255),
#                      Order_total INT,
#                      extra_cost_name varchar(300),
#                      extra_cost int,
#                      template varchar(500),
#                      sales_person varchar(300),
#                      discount_rate int,
#                      tax1 int,
#                      category varchar(300),
#                      businessaddress varchar(255),
#                      shipname varchar(255),
#                      shipaddress varchar(255),
#                      cpemail varchar(255),
#                      cpmobileforsms varchar(255),
#                      companyid int,
#                      Productserviceid int,
#                      customerid int,
#                      PRIMARY KEY(orderid),
#                      FOREIGN KEY (customerid) REFERENCES Customer (customerid) ON DELETE CASCADE,
#                      FOREIGN KEY (Productserviceid) REFERENCES Productservice (Productserviceid) ON DELETE CASCADE,
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
#                 """)      

# fbcursor.execute("""
#                  create table storingproduct(
#                      storingproductid int AUTO_INCREMENT,
#                      Productserviceid int 
#                      orderid int,
#                      estimateid int,
#                      invoiceid int,
#                      companyid int,
#                      sku varchar(255),
#                      category varchar(255),
#                      name varchar(255),
# 		             description varchar(255),
#                      status varchar(255),
#                      unitprice int,
# 		             peices varchar(255),
#                      cost int,
#                      taxable varchar(255),
#                      priceminuscost int,
#                      serviceornot varchar(255),
#                      stock int,
#                      stocklimit int,
#                      warehouse varchar(255),
#                      privatenote varchar(255),
#                      image LONGBLOB,
#                      PRIMARY KEY(storingproductid),
#                      FOREIGN KEY (companyid) REFERENCES Company (companyid) ON DELETE CASCADE)
                   
#                 """)       
           

           
