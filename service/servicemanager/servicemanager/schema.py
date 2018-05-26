import graphene
import graphql_jwt
import cockpit.schema


class Query(cockpit.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(cockpit.schema.Mutation, graphene.ObjectType):
    # Authentication
    # Fetch Token
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # Verify token
    verify_token = graphql_jwt.Verify.Field()
    # Get new token
    refresh_token = graphql_jwt.Refresh.Field()
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)