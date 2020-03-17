from firebase import firebase
firebase =firebase.FirebaseApplication('https://tesseract-23.firebaseio.com/',None)
data={
    'Name':'Piyush'
}
result=firebase.post('licence_plates',data)