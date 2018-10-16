from SOSial import ma
from SOSial.Models.user import UserModel
from marshmallow import Schema, fields, validate
from marshmallow_sqlalchemy import field_for


class UserSchema(ma.ModelSchema):

    user_id = field_for(UserModel, "user_id")
    username = field_for(UserModel, "username",
                         required=True,
                         partial=True,
                         validate=[validate.Length(min=1, max=36)]
                         )
    password = field_for(UserModel, "password",
                         required=True,
                         partial=True,
                         validate=[validate.Length(min=6, max=36)],
                         load_only=True
                         )
    first_name = field_for(UserModel, "first_name",
                           partial=True,
                           data_key="first_name",
                           required=False,
                           validate=[validate.Length(min=1, max=80)]
                           )
    last_name = field_for(UserModel, "last_name",
                          required=True,
                          partial=True,
                          validate=[validate.Length(min=1, max=80)]
                          )
    email = field_for(UserModel, "email", required=True,
                      partial=True,
                      validate=validate.Email(error='Not a valid email address')
                      )
    mobile = field_for(UserModel, "mobile",
                       required=True,
                       partial=True,
                       validate=[validate.Length(min=1, max=20)]
                       )
    dtm_added = field_for(UserModel, "dtm_added", load_only=True)

    class Meta:
        model = UserModel
        strict = True


