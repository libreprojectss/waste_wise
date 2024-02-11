import vine,{errors} from "@vinejs/vine";

class Base_Validator{
    constructor(){
        this.schema=vine.object({})
    }
    validate=async(data)=>{
        try {
            const validator = vine.compile(this.schema);
            const output = await validator.validate(data);
            return output
          } catch (error) {
            if (error instanceof errors.E_VALIDATION_ERROR) {
                throw error.messages[0]
            }
            else{
                console.log(error)
            }
          }
    }
}

export default Base_Validator