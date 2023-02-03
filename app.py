from hands_detection import HandsDetection
#from pose_detection import PoseDetection
#from holistic_detection import HolisticDetection

def main():
    choise_input = input("1:Hands Detection, 2:Pose Detection, 3:Holistic Detection =>")

    if choise_input == '1':
        detector = HandsDetection()

    elif choise_input == '2':
        #detector = PoseDetection()
        pass
    elif choise_input == '3':
        #detector = HolisticDetection()
        pass
    else:
        print('Tekrar input gir lütfen!')

if __name__ == '__main__':
    main()

