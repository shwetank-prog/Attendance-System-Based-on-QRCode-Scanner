# import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Users\shwetank\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import cv2
from pyzbar.pyzbar import decode

rows = [[1,2,3]]
print(type(rows))
    # cam = cv2.VideoCapture(0)
    # cv2.namedWindow("test")
    # img_counter = 0
    #
    # while True:
    #     ret, frame = cam.read()
    #     if not ret:
    #         print("failed to grab frame")
    #         break
    #     cv2.imshow("test", frame)
    #
    #     k = cv2.waitKey(1)
    #     if k%256 == 27:
    #         # ESC pressed
    #         print("Escape hit, closing...")
    #         break
    #     elif k%256 == 32:
    #         # SPACE pressed
    #         img_name = "opencv_frame_{}.jpeg".format(img_counter)
    #         cv2.imwrite(img_name, frame)
    #         print("{} written!".format(img_name))
    #         img_counter += 1
    #
    # cam.release()
    #
    # cv2.destroyAllWindows()
# def StoreAttend():
#     if value_inside.get() == 'Python':
#         fields = ['Data', 'Date','Subject']
#         rows = [[Data, date1.date(), value_inside.get()]]
#         # rows = [str(Data), str(date1)]
#         filename = "Attendence/records_python_"+str(date1.date())+".csv"
#         with open(filename, 'a+', newline="") as csvfile:
#             csvwriter = csv.writer(csvfile)
#             # csvwriter.writerow(fields)
#             csvwriter.writerows(rows)
#         csvfile.close()
#     elif value_inside.get() == 'Microprocessor':
#         fields = ['Data', 'Date', 'Subject']
#         rows = [[Data, date1.date(), value_inside.get()]]
#         # rows = [str(Data), str(date1)]
#         filename = "Attendence/records_micro_"+str(date1.date())+".csv"
#         with open(filename, 'a+', newline="") as csvfile:
#             csvwriter = csv.writer(csvfile)
#             # csvwriter.writerow(fields)
#             csvwriter.writerows(rows)
#     elif value_inside.get() == 'Maths':
#         fields = ['Data', 'Date', 'Subject']
#         rows = [[Data, date1.date(), value_inside.get()]]
#         # rows = [str(Data), str(date1)]
#         filename = "Attendence/records_maths_"+str(date1.date())+".csv"
#         with open(filename, 'a+', newline="") as csvfile:
#             csvwriter = csv.writer(csvfile)
#             # csvwriter.writerow(fields)
#             csvwriter.writerows(rows)
#     elif value_inside.get() == 'Operating System':
#         fields = ['Data', 'Date', 'Subject']
#         rows = [[Data, date1.date(), value_inside.get()]]
#         # rows = [str(Data), str(date1)]
#         filename = "Attendence/records_os_"+str(date1.date())+".csv"
#         with open(filename, 'a+', newline="") as csvfile:
#             csvwriter = csv.writer(csvfile)
#             # csvwriter.writerow(fields)
#             csvwriter.writerows(rows)
#     return 1
# def stats():
#
