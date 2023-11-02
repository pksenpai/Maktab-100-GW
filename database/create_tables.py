from connect_to_db import connect


def create_table_patient():
    conn, cur, local_connection = connect(None, None)
    query = """
    CREATE TABLE patient (
        patient_id SERIAL PRIMARY KEY ,
        first_name VARCHAR(50) NOT NULL ,
        last_name VARCHAR(50)NOT NULL ,
        gender VARCHAR(15) NOT NULL ,    
        Birth_date VARCHAR(15) NOT NULL ,
        phone VARCHAR(15) NOT NULL ,
        email VARCHAR(50),
        address TEXT NOT NULL , 
        national_code INT NOT NULL UNIQUE ,
        health_insurance_id VARCHAR(50),
        password VARCHAR(255) NOT NULL ,
        login_status BOOLEAN NOT NULL 
    );
    """
    cur.execute(query)
    conn.commit()


def create_table_doctor():
    conn, cur, local_connection = connect(None, None)
    query = """
    CREATE TABLE doctor (
        doctor_id SERIAL PRIMARY KEY ,
        first_name VARCHAR(50) NOT NULL ,
        last_name VARCHAR(50)NOT NULL ,
        gender VARCHAR(15) NOT NULL ,    
        Birth_date VARCHAR(15) NOT NULL ,
        phone VARCHAR(15) NOT NULL ,
        email VARCHAR(50),
        address TEXT NOT NULL ,
        national_code VARCHAR(20) UNIQUE ,
        medical_council_code INT NOT NULL UNIQUE ,
        specialization VARCHAR(50),
        password VARCHAR(255) NOT NULL ,
        login_status BOOLEAN NOT NULL 
    );
    """
    cur.execute(query)
    conn.commit()


def create_table_appointment():
    conn, cur, local_connection = connect(None, None)
    query = """
    CREATE TABLE appoinment (
        appoinment_id SERIAL PRIMARY KEY ,
        patient_id INT,
        FOREIGN KEY (patient_id) REFERENCES patient (patient_id) ,
        doctor_id INT,
        FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id) ,
        date_time TIMESTAMP NOT NULL,
        reason  VARCHAR(100)
    );
    """
    cur.execute(query)
    conn.commit()


def create_table_patient_history():
    conn, cur, local_connection = connect(None, None)
    query = """
    CREATE TABLE patient_history (
        patient_history_id SERIAL PRIMARY KEY,
        patient_id INT,
        FOREIGN KEY (patient_id) REFERENCES patient (patient_id),
        doctor_id INT,
        FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id),
        diagnosis TEXT,
        drug_used TEXT,    
        prescription TEXT,
        date TIMESTAMP NOT NULL,
        Note TEXT
    );
    """
    cur.execute(query)
    conn.commit()


def create_table_health_insurance():
    conn, cur, local_connection = connect(None, None)
    query = """
    CREATE TABLE health_insurance (
        health_insurance_id SERIAL PRIMARY KEY,
        company VARCHAR NOT NULL UNIQUE , 
        address TEXT,
        phone VARCHAR(15) NOT NULL,    
        email VARCHAR(50),
        payment_discount_percentage INT
    );
    """
    cur.execute(query)
    conn.commit()


def create_table_patient_bill():
    conn, cur, local_connection = connect(None, None)
    query = """
    CREATE TABLE patient_bill (
        patient_bill_id SERIAL PRIMARY KEY ,
        patient_history_id INT,
        FOREIGN KEY (patient_history_id) REFERENCES patient_history (patient_history_id) ,
        total_cost INT ,
        patient_payable INT ,    
        insurance_contribution INT ,
        date TIMESTAMP,
        transaction_status BOOLEAN NOT NULL
    );
    """
    cur.execute(query)
    conn.commit()


if __name__ == '__main__':
    create_table_doctor(True)
